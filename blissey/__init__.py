# -*- coding: utf-8 -*-

import json
import logging.config
import os

__all__ = ['application', 'configuration']


def get_configuration(application_name):

    configuration_file_path = os.environ[
        application_name.upper() + '_CONFIGURATION_FILE_PATH']

    with open(configuration_file_path, 'r') as file:
        parsed_configuration = json.loads(file.read())

    return parsed_configuration


configuration = get_configuration(application_name=__name__)
logging.config.dictConfig(config=configuration['logging'])
