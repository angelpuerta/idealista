import json
import logging

import requests

from .exceeded_request import ExceededRequest
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

    def query_page(self, search_request: SearchRequest) -> SearchPage:
        return self._get_page(search_request)

    def query_iterator(self, search_request: SearchRequest, limit: int = None) -> PropertyIter:
        return PropertyIter(search_request, self._get_page, limit)

    def _get_page(self, search_request: SearchRequest) -> SearchPage | SearchError | ExceededRequest:
        country_url = f'{self.uri}/{search_request.country}/search'
        logging.debug(search_request)
        response = self._search_page(country_url, search_request)
        if isinstance(response, ExceededRequest):
            logging.debug(f"The number of requests have exceeded the token")
            config.next_credentails()
            authenticationSession.expire_token()
            return self._search_page(country_url, search_request)
        return response

    
    def _search_page(self, country_url, search_request)-> SearchPage | SearchError | ExceededRequest:
        response = requests.post(country_url, headers=self._auth_header(), params=search_request.params)
        if response.status_code == 200:
            page = SearchPage(**response.json())
            logging.debug(page)
            return page
        if response.status_code == 429:
            return ExceededRequest()
        logging.error(f"For the following search request we had the code {response.status_code}")
        logging.error(search_request)
        error = SearchError(response.status_code, response.json())
        logging.error(error)
        return error

    def _auth_header(self):
        return {'Authorization': f'Bearer {authenticationSession.token}'}


search_service = SearchService()
