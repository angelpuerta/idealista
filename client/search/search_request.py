from client.search.query.geo_query import GeoQuery
from client.search.query.location_query import LocationQuery
from client.search.query.search_query import SearchQuery
from utils.utils import to_dict, parse_dict
import yaml


class SearchRequest:
    _query: SearchQuery
    _locationQuery: LocationQuery
    _geoQuery: GeoQuery
    _filters: dict = {}

    def __init__(self, query: SearchQuery, geo_query: LocationQuery | GeoQuery):
        self._query = query
        if isinstance(geo_query, GeoQuery):
            self._geoQuery = geo_query
        if isinstance(geo_query, LocationQuery):
            self.location_query = geo_query

    def get_query(self):
        return self._query

    def set_query(self, query: SearchQuery):
        self._query = query

    def get_location_query(self):
        return self._locationQuery

    def get_geo_query(self):
        return self._geoQuery

    def set_location_query(self, locationQuery: LocationQuery):
        if self._geoQuery:
            raise Exception("Cannot have a location and query search")
        self._locationQuery = locationQuery

    def set_geo_query(self, geoQuery: GeoQuery):
        if self._locationQuery:
            raise Exception("Cannot have a location and query search")
        self._geoQuery = geoQuery

    geo_query = property(get_geo_query, set_geo_query)
    location_query = property(get_location_query, set_location_query)
    query = property(get_query, set_query)

    @property
    def country(self):
        return self._query.country.value

    def add_filter(self, filter):
        if isinstance(filter, dict):
            self._filters = self._filters | filter
            return self._filters
        if isinstance(filter, object):
            self._filters = self._filters | filter.__dict__
            return self._filters

    @property
    def params(self):
        geo_query = self._geoQuery.to_dict() if self._geoQuery else to_dict(self._locationQuery)
        return to_dict(self._query) | geo_query | parse_dict(self._filters)

    def next_page(self):
        return self._query.next_page()

    def __str__(self):
        return yaml.dump(self, sort_keys=True)
