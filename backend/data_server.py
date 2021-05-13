"""
A Simple RPyC metadata server implementation.
"""

import logging
import json

from rpyc import Service


logger = logging.getLogger(__name__)


class PreziMetadataService(Service):
    """ Metadata service implementation. """
    def __init__(self, data_source):
        self.data_source = data_source
        self.json_data = None

        self.initialize()
    # end __init__()

    def initialize(self):
        """ Loads datasource. """
        with open(self.data_source, 'r') as handle:
            self.json_data = json.load(handle)
    # end initialize()

    def exposed_get_all_data(self):
        """ Get the full dataset. """
        return self.json_data
    # end exposed_get_all_data()

    def exposed_get_prezi_by_title(self, prezi_title):
        """ Returns all metadata corresponding to the given title. """
        for entry in self.json_data:
            if entry['title'] == prezi_title:
                return entry
        return None
    # end exposed_get_prezi_by_title
