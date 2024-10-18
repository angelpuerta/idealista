#!/bin/python
import time
import argparse
import sys
from digest.launcher import launch_all
from anacron import programmed_run
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Prevent the root logger from handling messages (to avoid duplicate outputs)
logger.propagate = False

if logger.hasHandlers():
    logger.handlers.clear()

# Create handler and set format
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s line %(lineno)d - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(handler)

# Argument parsing
parser = argparse.ArgumentParser(description="Run launch_all with or without a loop.")
parser.add_argument('--run-once', action='store_true', help='Run launch_all without the loop')
args = parser.parse_args()

if args.run_once:
    launch_all()
    sys.exit(0)


while True:
    programmed_run(launch_all)
    time.sleep(2*3600)


