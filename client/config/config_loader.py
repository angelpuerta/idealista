from pathlib import Path

import toml
from utils.decorator import singleton


@singleton
class Config:
    secret: str
    apiKey: str
    idealista_base_url: str
    idealista_url: str    
    credentials_index: int = 0
    credentials = []

    path = Path(__file__).parent.parent

    def __init__(self):
        self.load_from_config()

    def load_from_config(self):
        with open(self.path.joinpath('config.toml')) as file:
            contents = toml.load(file)
            self.credentials = contents['credentials']
            self.secret = self.credentials[self.credentials_index]['secret']
            self.apiKey = self.credentials[self.credentials_index]['apiKey']
            self.idealista_base_url = contents['api']['url']
            version = contents['api']['version']
            self.idealista_url = f'{self.idealista_base_url}/{version}'

    def next_credentails(self):
        if (self.credentials_index >= len(self.credentials)):
            self.credentials_index = 0
        else:
            self.credentials_index = self.credentials_index+ 1
        self.secret = self.credentials[self.credentials_index]['secret']
        self.apiKey = self.credentials[self.credentials_index]['apiKey']


config = Config()
