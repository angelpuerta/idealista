from pathlib import Path

import toml
from utils.decorator import singleton


@singleton
class Config:
    secret: str
    apiKey: str
    idealista_base_url: str
    idealista_url: str

    path = Path(__file__).parent.parent

    def __init__(self):
        self.load_from_config()

    def load_from_config(self):
        with open(self.path.joinpath('config.toml')) as file:
            contents = toml.load(file)
            credentials = contents['credentials']
            self.secret = credentials['secret']
            self.apiKey = credentials['apiKey']
            self.idealista_base_url = contents['api']['url']
            version = contents['api']['version']
            self.idealista_url = f'{self.idealista_base_url}/{version}'


config = Config()
