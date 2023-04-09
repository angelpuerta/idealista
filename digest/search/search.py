from typing import Iterator

from client.search.search_request import SearchRequest
from client.search.search_result import Property
from client.search.search_service import search_service
from digest.pipeline.pipeline import Pipeline
from utils.decorator import singleton


@singleton
class Search:
    def query(self, pipeline: Pipeline) -> Iterator[Property]:
        request = SearchRequest(pipeline.query, pipeline.geo_query)
        request.add_filter(pipeline.filters)
        return search_service.query_iterator(request, pipeline.limit)


search = Search()
