"""
    Minimalistic PreziMetadataClient implementation.
"""

import rpyc


class PreziMetadataClient:
    """ Client for the PreziMetadataService. """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conn = rpyc.connect(host, port, config={"allow_all_attrs": True})
    # end __init__()

    def get_all_data(self):
        """ Returns the full collection of data. """
        return self.conn.root.get_all_data()
    # end get_all_data()

    def get_prezi_by_title(self, title):
        """ Returns all metadata corresponding to the given title. """
        return self.conn.root.get_prezi_by_title(title)
    # end get_rezi_by_title
