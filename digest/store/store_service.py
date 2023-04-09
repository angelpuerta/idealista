import csv
from dataclasses import fields
from datetime import datetime
from pathlib import Path
from typing import Callable, Iterator

from client.search.search_result import Property
from digest.pipeline.pipeline import Pipeline
from digest.store.store import Store
from digest.store.store_type import StoreType
from utils.decorator import singleton
from utils.utils import to_dict
import pandas as pd


@singleton
class StoreService:
    path = Path(__file__).parent.parent

    def store(self, pipeline: Pipeline, iterator: Iterator[Property]):
        store = pipeline.store
        self.store_functions[store.type](store, iterator)

    def store_csv(self, store: Store, iterator: Iterator[Property]):
        properties_fields = list(map(lambda x: x.name, fields(Property))) + ['created']
        path = self.path.joinpath(store.output)
        mode = 'a' if path.is_file() else 'w'
        with open(path, mode) as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=properties_fields)

            if mode == 'w':
                writer.writeheader()

            for property in iterator:
                writer.writerow(to_dict(property) | {'created': datetime.now()})
        self.csv_remove_duplicates(store)

    def csv_remove_duplicates(self, store: Store):
        path = self.path.joinpath(store.output)
        df = pd.read_csv(path)
        merged_df = df.sort_values('created').groupby('propertyCode').first()
        merged_df.to_csv(path, index=False)

    @property
    def store_functions(self):
        return {
            StoreType.CSV: self.store_csv
        }


store_service = StoreService()
