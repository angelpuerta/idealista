from dataclasses import dataclass

from client.search.query.geo_query import GeoQuery
from client.search.query.search_query import SearchQuery
from digest.store.store import Store


@dataclass
class Pipeline:
    name: str
    query: SearchQuery
    geo_query: GeoQuery
    filters: dict
    store: Store
    limit: int | None
