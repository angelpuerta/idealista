import os
from pathlib import Path

import pandas as pd

from digest.pipeline.pipeline import Pipeline
from utils.decorator import singleton


@singleton
class RunService:
    path = Path(__file__).parent.parent

    def run(self, pipeline: Pipeline):
        self.run_functions[pipeline.run.function](pipeline.run.arg)

    def join_csv(self, path:str):
        path = self.path.joinpath(path)
        concatenated_data = pd.DataFrame()

        for file_name in os.listdir(path):
            if file_name.endswith(".tsv"):
                file_path = os.path.join(path, file_name)
                data = pd.read_csv(file_path, sep='\t')
                concatenated_data = pd.concat([concatenated_data, data])

        grouped_data = concatenated_data.sort_values("created").groupby('propertyCode').tail(1)
        deduplicated_data = grouped_data.drop_duplicates(subset="propertyCode", inplace=False)
        output_file_path = os.path.join(path, "output.csv")
        deduplicated_data.to_csv(output_file_path, sep='\t', mode='w+', index=False)

    @property
    def run_functions(self):
        return {
            "join_csv": self.join_csv
        }


run_service = RunService()
