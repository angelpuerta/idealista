import json
import logging

import requests

from .property_iterator import PropertyIter
from .search_error import SearchError
from .search_request import SearchRequest
from .search_result import SearchPage
from ..authentication import authenticationSession
from ..config import config

from utils.decorator import singleton


@singleton
class SearchService:
    uri = config.idealista_url
    token = authenticationSession.token

    def query_page(self, search_request: SearchRequest) -> SearchPage:
        return self._get_page(search_request)

    def query_iterator(self, search_request: SearchRequest, limit: int = None) -> PropertyIter:
        property = PropertyIter(search_request, self._get_page, limit)
        return property

    def _get_page(self, search_request: SearchRequest) -> SearchPage | SearchError:
        country_url = f'{self.uri}/{search_request.country}/search'
        logging.debug(search_request)
        response = requests.post(country_url, headers=self._auth_header(), params=search_request.params)
        if response.status_code == 200:
            page = SearchPage(**response.json())
            logging.debug(page)
            return page
        error = SearchError(response.status_code, response.json()['message'])
        logging.error(error)
        return error

    def _auth_header(self):
        return {'Authorization': f'Bearer {self.token}'}


search_service = SearchService()
