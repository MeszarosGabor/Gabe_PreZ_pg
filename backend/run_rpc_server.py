"""
    Main Runner of the PreziData Server.
"""
import logging
import sys

from rpyc.utils.server import ThreadedServer
from data_server import PreziMetadataService

logger = logging.getLogger()
logger.setLevel(logging.INFO)
loghandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(levelname)s] - %(asctime)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:S')
loghandler.setFormatter(formatter)
logger.addHandler(loghandler)

# TODO: finalize lib structure for data json.
# TODO: make path OS agnostic!
s = ThreadedServer(PreziMetadataService('../data_source/prezis.json'),
                   port=18871,
                   protocol_config={"allow_all_attrs": True})
print("Starting PreziMetadataService...")
s.start()
