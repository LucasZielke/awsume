import logging
import sys

from . import app
from .lib.logger import logger


def run_awsume(argument_list):
    awsume = app.Awsume()
    awsume.run(argument_list)


def main():
    try:
        if "--debug" in sys.argv:
            logger.setLevel(logging.DEBUG)
            logger.debug("Debug logs are visible")
        elif "--info" in sys.argv:
            logger.setLevel(logging.INFO)
            logger.info("Info logs are visible")
        logger.debug("Executing awsume")
        run_awsume(sys.argv[1:])
    except KeyboardInterrupt:
        pass
