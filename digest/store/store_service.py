import csv
import logging
import os
from dataclasses import fields
from datetime import datetime
from pathlib import Path
from typing import Iterator

from client.search.exceeded_request import ExceededRequest
from client.search.property_iterator import PropertyIter
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

    def store(self, pipeline: Pipeline, iterator: PropertyIter):
        store = pipeline.store
        self.store_functions[store.type](pipeline, iterator)

    def store_tsv(self, pipeline:Pipeline, iterator: PropertyIter):
        logging.info(f"Storing the pipeline {pipeline.name}")
        properties_fields = list(map(lambda x: x.name, fields(Property))) + ['created']
        path = self.path.joinpath(pipeline.store.output)

        if not os.path.exists(path):
            os.makedirs(path)

        path = path.joinpath(time_stamp(pipeline) + ".tsv")
        with open(path, 'w', encoding='utf-8', newline="") as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=properties_fields)
            writer.writeheader()

            try:
                for state in iterator:
                    state = purge_strings(state.__dict__)
                    writer.writerow(state | {'created': datetime.now()})
                logging.info(f"Store complete for {pipeline.name}")
            except StopIteration as e:
                logging.warning(f"The limit for the query has been reached {e}")
            except Exception as e:
                logging.error(e)

    @property
    def store_functions(self):
        return {
            StoreType.TSV: self.store_tsv
        }


store_service = StoreService()
