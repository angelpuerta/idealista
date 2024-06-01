import logging

from digest.pipeline.pipeline_reader import pipelines
from digest.run.run_service import run_service
from digest.search.search import search
from digest.store.store_service import store_service


def launch(name: str):
    if name not in pipelines:
        raise Exception(f'Pipeline {name} not in pipelines.yaml')
    pipeline = pipelines[name]
    launch_pipeline(pipeline)


def launch_pipeline(pipeline):
    logging.info(f'Executing pipe {pipeline.name}')
    if pipeline.query:
        result = search.query(pipeline)
        store_service.store(pipeline, result)
    if pipeline.run:
        run_service.run(pipeline)


def launch_all():
    logging.info(f'Launching all pipelines')
    for pipeline in pipelines.values():
        try:
            launch_pipeline(pipeline)
        except Exception as e:
            logging.error(e)
            return
    logging.info(f'Pipelines completed')



