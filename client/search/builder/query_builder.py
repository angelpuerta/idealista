from dacite import from_dict

from client.search.enum.country import Country
from client.search.enum.locale import Locale
from client.search.enum.operation import Operation
from client.search.enum.property_type import PropertyType
from client.search.query.search_query import SearchQuery


def sales_spain() -> SearchQuery:
    data = {
        'country': Country.SPAIN,
        'operation': Operation.SALE,
        'propertyType': PropertyType.HOMES,
        'locale': Locale.ES,
    }
    return from_dict(data_class=SearchQuery, data=data)


def rent_spain() -> SearchQuery:
    data = {
        'country': Country.SPAIN,
        'operation': Operation.RENT,
        'propertyType': PropertyType.HOMES,
        'locale': Locale.ES,
    }
    return from_dict(data_class=SearchQuery, data=data)
