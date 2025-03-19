import os
from pathlib import Path

import pandas as pd

import logging
from digest.pipeline.pipeline import Pipeline
from digest.run.send_telegram import send_telegram_notification
from digest.run.store_drive import store_drive
from utils.decorator import singleton


@singleton
class RunService:
    path = Path(__file__).parent.parent

    def run(self, pipeline: Pipeline):
        self.run_functions[pipeline.run.function](pipeline.run.arg)

    def join_csv(self, path:str):
        logging.info(f"Running join csv for {path}")
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
        logging.info(f"Completed join csv for {path}")

    def store_drive(self, args: str):
        logging.info(f"Running store drive for {args}")
        args = args.split(" ")
        from_path = args[0]
        to_path = args[1]

        store_drive(from_path, to_path)
        logging.info(f"Completed store drive for {args}")

    def send_telegram_notification(self, args: str):
        logging.info(f"Running send telegram annotation with message {args}")
        response  = send_telegram_notification(args)
        logging.info(response)
        logging.info(f"Completed telegram annotation with message {args}")

    @property
    def run_functions(self):
        return {
            "join_csv": self.join_csv,
            "store_drive": self.store_drive,
            "send_telegram_notification": self.send_telegram_notification
        }



run_service = RunService()
