"""
PreziMetadata  Service implementaton.
"""

import json

from flask import request
from flask_restful import Resource


class PreziMetadata(Resource):
    """ Metadata service implementation. """
    def __init__(self, data_source='../data_source/prezis.json'):
        self.data_source = data_source
        self.json_data = None
        self.sorted_json_data = None  # only sort it once

        self.initialize()
    # end __init__()

    def initialize(self):
        """ Loads datasource. """
        with open(self.data_source, 'r') as handle:
            self.json_data = json.load(handle)
        self.sorted_json_data = sorted(self.json_data,
                                       key=lambda entry: entry['createdAt'])
    # end initialize()

    def get(self):
        """
            Get metadata for a single item. Default for all data returned.
            Return all entries in either sorted or unsorted fashion
            depending on the corresponding flag.
        """
        title = request.args.get('title', '')
        is_sorted = request.args.get('sorted', False)
        print(request.args)
        if not title:
            if is_sorted:
                return self.sorted_json_data
            return self.json_data
        for entry in self.json_data:
            if entry['title'] == title:
                return entry
        return {'result': 'not found'}
    # end get()
