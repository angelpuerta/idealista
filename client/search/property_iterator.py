from typing import Iterator, Callable

import dacite

from client.search.enum.operation import Operation
from client.search.enum.property_type import PropertyType
from client.search.enum.status import Status
from client.search.search_error import SearchError
from client.search.search_request import SearchRequest
from client.search.search_result import SearchPage, Property, DetailedType


class PropertyIter:
    _search_request: SearchRequest
    _current_page: SearchPage
    _propertyIterator: Iterator[Property]
    _get_page: Callable[[SearchRequest], SearchPage | SearchError]
    _count: int = 0
    _limit: int = None

    def __init__(self, initial_search_request: SearchRequest,
                 get_page: Callable[[SearchRequest], SearchPage | SearchError],
                 limit: int = None):
        self._search_request = initial_search_request
        self._get_page = get_page
        self._limit = limit
        self.get_current_page()

    def __iter__(self):
        return self

    def __next__(self):
        next_property = next(self._propertyIterator, None)
        if self._limit_reached():
            raise StopIteration
        if not next_property and not self.is_next_page():
            raise StopIteration
        if not next_property and self.is_next_page():
            self.next_page()
            next_property = next(self._propertyIterator, None)
        if not next_property:
            raise ValueError("Impossible path has been reached")
        self._count = self._count + 1
        return dacite.from_dict(data_class=Property, data=next_property,
                                config=dacite.Config(
                                    type_hooks={Operation: Operation, DetailedType: DetailedType, Status: Status,
                                                PropertyType: PropertyType}))

    def _limit_reached(self):
        return self._limit and self._count + 1 >= self._limit

    def is_next_page(self):
        return self._current_page.actualPage + 1 <= self._current_page.totalPages

    def next_page(self):
        self._search_request.next_page()
        self.get_current_page()

    def get_current_page(self):
        result = self._get_page(self._search_request)
        if not result:
            raise Exception(str(result))
        self._current_page = result
        self._propertyIterator = self._current_page.elementList.__iter__()
