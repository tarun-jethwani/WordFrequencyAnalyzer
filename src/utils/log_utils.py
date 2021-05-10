""" A logger and its configuration

 This module defines logger, along with respective handler, directory
 and name of the log file and sets all configuration parameters for logs
 like log_level, filemode, maxBytes after which to rotate logs, backup count

 """

import logging
import os
from logging.handlers import RotatingFileHandler

from .config import DEBUG_CONTROL, LOG_MODE

LOG_FILENAME = "logs/run.log"

# create log directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, filemode="a",
                    format="%(asctime)s %(filename)-10s %(funcName)-12s"
                           " %(levelname)-8s %(message)s")

logger = logging.getLogger(__name__)

# add a rotating handler
handler = RotatingFileHandler(LOG_FILENAME, maxBytes=1000000, backupCount=10)
logger.addHandler(handler)

# disable debug logs based on control values
# value can be overwritten in config.py
if DEBUG_CONTROL is not True:
    # 10 is the numerical value of DEBUG level
    logging.disable(10)

# disable logs based on following value
# value can be overwritten in config.py
if LOG_MODE is not True:
    logger.disabled = True
