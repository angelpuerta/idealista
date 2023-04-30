import csv
import os
from dataclasses import fields
from datetime import datetime
from pathlib import Path
from typing import Iterator

from client.search.search_result import Property
from digest.pipeline.pipeline import Pipeline
from digest.store.store_type import StoreType
from utils.decorator import singleton
from utils.utils import to_dict


def time_stamp(pipeline: Pipeline) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f'{pipeline.name}_{timestamp}'


@singleton
class StoreService:
    path = Path(__file__).parent.parent

    def store(self, pipeline: Pipeline, iterator: Iterator[Property]):
        store = pipeline.store
        self.store_functions[store.type](pipeline, iterator)

    def store_tsv(self, pipeline:Pipeline, iterator: Iterator[Property]):
        properties_fields = list(map(lambda x: x.name, fields(Property))) + ['created']
        path = self.path.joinpath(pipeline.store.output)

        if not os.path.exists(path):
            os.makedirs(path)

        path = path.joinpath(time_stamp(pipeline) + ".tsv")
        with open(path, 'w', encoding='utf-8', newline="") as file:
            writer = csv.DictWriter(file, delimiter='\t', fieldnames=properties_fields)
            writer.writeheader()

            for estate in iterator:
                writer.writerow(estate.__dict__ | {'created': datetime.now()})

    @property
    def store_functions(self):
        return {
            StoreType.TSV: self.store_tsv
        }


store_service = StoreService()
