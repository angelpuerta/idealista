from dataclasses import dataclass

from client.search.query.geo_query import GeoQuery
from client.search.query.search_query import SearchQuery
from digest.run.command import Command
from digest.store.store import Store


@dataclass
class Pipeline:
    name: str
    query: SearchQuery | None
    geo_query: GeoQuery | None
    filters: dict | None
    store: Store | None
    limit: int | None
    run: Command | None
