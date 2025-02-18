import csv
import logging
import os
from dataclasses import fields
from datetime import datetime
from pathlib import Path
from typing import Iterator


from client.search.search_result import Property
from digest.pipeline.pipeline import Pipeline
from digest.store.store_type import StoreType
from utils.decorator import singleton

def purge_strings(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, str):
            dictionary[key] = value.replace('\n', ' ').replace('\t', ' ')
    return dictionary

def time_stamp(pipeline: Pipeline) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f'{pipeline.name}_{timestamp}'


@singleton
class StoreService:
    path = Path(__file__).parent.parent

    def store(self, pipeline: Pipeline, iterator: Iterator):
        store = pipeline.store
        return self.store_functions[store.type](pipeline, iterator)

    def load(self, pipeline, path):
        store = pipeline.store
        return self.load_functions[store.type](path)

    def model_output_fields(self, pipeline: Pipeline):
       if not pipeline.models:
           return []
       return [model.output for model in pipeline.models]

    def store_tsv(self, pipeline:Pipeline, iterator: Iterator):
        logging.info(f"Storing the pipeline {pipeline.name}")
        properties_fields = list(map(lambda x: x.name, fields(Property))) + ['created'] + self.model_output_fields(pipeline)
        path = self.path.joinpath(pipeline.store.output)

        if not os.path.exists(path):
            os.makedirs(path)

        path = path.joinpath(time_stamp(pipeline) + ".tsv")
        with open(path, 'w', encoding='utf-8', newline="") as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=properties_fields)
            writer.writeheader()

            try:
                for state in iterator:
                    if hasattr(state, "__dict__"):
                        state = purge_strings(state.__dict__)
                    else:
                        state = purge_strings(state)
                    writer.writerow(state | {'created': datetime.now()})
                logging.info(f"Store complete for {pipeline.name}")
            except StopIteration as e:
                logging.warning(f"The limit for the query has been reached {e}")
            except Exception as e:
                logging.error("There has been an error while parsing the properties")
                logging.error(e)
        return path
    
    def load_tsv(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='\t')
            return [row for row in reader]
        
    @property
    def store_functions(self):
        return {
            StoreType.TSV: self.store_tsv
        }

    @property
    def load_functions(self):
        return {
            StoreType.TSV: self.load_tsv
        }

store_service = StoreService()
