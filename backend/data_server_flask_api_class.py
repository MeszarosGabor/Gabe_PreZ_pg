"""
PreziMetadata Flask Service implementaton.
"""

import json
import os
from datetime import datetime
from flask import request
from flask_restful import Resource


class PreziMetadata(Resource):
    """ Metadata service implementation. """
    DEFAULT_SOURCE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  '..', 'data_source', 'prezis.json')

    def __init__(self, data_source=None):
        self.data_source = data_source if data_source else self.DEFAULT_SOURCE
        self.json_data = None
        self.sorted_json_data = None  # only sort it once

        self.initialize()
    # end __init__()

    def initialize(self):
        """ Loads datasource. """
        with open(self.data_source, 'r') as handle:
            self.json_data = json.load(handle)
        self.sorted_json_data =\
            sorted(self.json_data,
                   key=lambda entry: datetime.strptime(entry['createdAt'],
                                                       "%B %d, %Y"))
    # end initialize()

    def get(self):
        """
            Get metadata for a single item. Default for all data returned.
            Return all entries in either sorted or unsorted fashion
            depending on the corresponding flag.
        """
        title = request.args.get('title', '')
        is_sorted = request.args.get('sorted', False)
        desc = request.args.get('desc', False)

        # Returning all entries
        if not title:
            if is_sorted:
                if desc:
                    return self.sorted_json_data[::-1]
                return self.sorted_json_data
            return self.json_data

        # Returning entries matching the title (no sorting)
        hits = []
        for entry in self.json_data:
            if entry['title'] == title:
                hits.append(entry)
        return hits
    # end get()
