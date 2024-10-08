#!/bin/python
import sys
import time

from digest.launcher import launch_all
from anacron import programmed_run
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

while True:
    programmed_run(launch_all)
    time.sleep(2*3600)

