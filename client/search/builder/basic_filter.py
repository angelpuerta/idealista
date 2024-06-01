from dacite import from_dict

from client.search.enum.since_date import SinceDate
from client.search.filter.basic_filter import BasicFilter


def basic_filter(min_price: float, min_size: float, max_price: float = None, max_size: float = None,
                 since_date: SinceDate = SinceDate.LAST_WEEK) -> BasicFilter:
    data = {
        'minSize': min_size,
        'minPrice': min_price,
        'maxPrice': max_price,
        'maxSize': max_size,
        'sinceDate': since_date
    }
    return from_dict(data_class=BasicFilter, data=data)
