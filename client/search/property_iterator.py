from typing import Iterator, Callable

import dacite

import logging

from client.authentication.authentication_service import authenticationSession
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
        if self._limit is not None and self._count >= self._limit:
            raise StopIteration

        next_property = next(self._propertyIterator, None)

        # If current page is exhausted, try to get the next page
        while next_property is None and self.is_next_page():
            logging.info("Retrieving next page")
            self.next_page()
            next_property = next(self._propertyIterator, None)

        # If still None, we are truly done
        if next_property is None:
            authenticationSession.expire_token()
            logging.info("Stopping retrieve - no more properties found")
            raise StopIteration

        self._count += 1
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
