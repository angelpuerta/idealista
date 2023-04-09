import csv
from pathlib import Path

from utils.decorator import singleton


@singleton
class CityLoader:
    _city_coordinates = {}
    file_path = Path(__file__).parent.joinpath(Path('./cities.csv'))

    def __init__(self):
        self.load_city_coordinates()

    def load_city_coordinates(self):
        with open(self.file_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                city = row['Población']
                latitude = self.replace_parse_number(row['Latitud'])
                longitude = self.replace_parse_number(row['Longitud'])

                self._city_coordinates[city] = {'latitude': latitude, 'longitude': longitude}

    def replace_parse_number(self, string: str) -> float:
        return float(string.replace(",", "."))

    @property
    def city_coordinates(self):
        return self._city_coordinates


city_coordinates = CityLoader().city_coordinates
