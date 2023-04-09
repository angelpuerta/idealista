import logging
from pathlib import Path

import dacite
import yaml
from dacite import from_dict

from client.search.builder.geo_query_builder import from_city
from client.search.enum.country import Country
from client.search.enum.locale import Locale
from client.search.enum.operation import Operation
from client.search.enum.property_type import PropertyType
from client.search.query.geo_query import GeoQuery
from client.search.query.search_query import SearchQuery
from digest.pipeline.pipeline import Pipeline
from digest.store.store import Store
from digest.store.store_type import StoreType


def map_pipeline(yaml_definition: dict) -> Pipeline:
    name = yaml_definition['name']
    search = yaml_definition['search']
    query = search['query']
    geo_query = search['geoQuery']
    filters = search['filters']
    store = yaml_definition['store']
    limit = search['limit']

    if 'city' in geo_query:
        geo_query = from_city(geo_query['city'], geo_query['distance'])
    else:
        geo_query = from_dict(data_class=GeoQuery, data=geo_query)
    query = from_dict(data_class=SearchQuery, data=query,
                      config=dacite.Config(type_hooks={Country: Country, Locale: Locale, Operation: Operation,
                                                       PropertyType: PropertyType}))
    store = from_dict(data_class=Store, data=store,
                      config=dacite.Config(type_hooks={StoreType: StoreType}))

    return from_dict(data_class=Pipeline,
                     data={
                         'name': name,
                         'query': query,
                         'geo_query': geo_query,
                         'filters': filters,
                         'store': store,
                         'limit': limit
                     })


path = Path(__file__).parent.parent

with open(path.joinpath('pipelines.yaml')) as file:
    pipelines = yaml.load(file, Loader=yaml.FullLoader)
    pipelines = [map_pipeline(pipeline) for pipeline in pipelines['pipelines']]
    logging.debug(pipelines)
    pipelines = {pipeline.name: pipeline for pipeline in pipelines}
