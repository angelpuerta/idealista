import logging

from digest.pipeline.pipeline_reader import pipelines
from digest.search.search import search
from digest.store.store_service import store_service


def launch(name: str):
    logging.debug(f'Executing pipe {name}')
    if name not in pipelines:
        raise Exception(f'Pipeline {name} not in pipelines.yaml')
    pipeline = pipelines[name]
    result = search.query(pipeline)
    store_service.store(pipeline, result)
