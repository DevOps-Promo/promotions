"""
Package: service
Package for the APPlication models and service routes
This module creates and configures the Flask APP and sets up the logging
and SQL database
"""
# import os
import sys
import logging
from flask import Flask
# Import the rutes After the Flask APP is created
from service import service, models

# Create Flask APPlication
APP = Flask(__name__)
APP.config.from_object('config')


# Set up logging for production
if __name__ != '__main__':
    GUNICORN_LOGGER = logging.getLogger('gunicorn.error')
    APP.logger.handlers = GUNICORN_LOGGER.handlers
    APP.logger.setLevel(GUNICORN_LOGGER.level)
    APP.logger.propagate = False
    # Make all log formats consistent
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s",
                                  "%Y-%m-%d %H:%M:%S %z")
    for handler in APP.logger.handlers:
        handler.setFormatter(formatter)
    APP.logger.info('Logging handler established')

APP.logger.info(70 * "*")
APP.logger.info("  P R O M O T I O N S   S E R V I C E   R U N N I N G  ".center(70, "*"))
APP.logger.info(70 * "*")

try:
    service.init_db()  # make our sqlalchemy tables
except Exception as error:
    APP.logger.critical("%s: Cannot continue", error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

APP.logger.info("Service inititalized!")
