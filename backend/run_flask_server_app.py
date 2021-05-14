"""
PreziMetadata Flask Service main runner.
"""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from data_server_flask_api_class import PreziMetadata

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(PreziMetadata,
                 "/search",
                 "/search/",
                 )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18871, debug=True)
