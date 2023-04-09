from dataclasses import dataclass

from client.search.enum.country import Country
from client.search.enum.locale import Locale
from client.search.enum.operation import Operation
from client.search.enum.property_type import PropertyType


@dataclass
class SearchQuery:
    country: Country
    operation: Operation
    propertyType: PropertyType
    locale: Locale
    maxItems: int = 50
    numPage: int = 1
    order: str = None
    sort: str = None
    hasMultimedia: bool = None

    def next_page(self):
        self.numPage = self.numPage + 1
        return self.numPage

