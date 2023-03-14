# Standard python imports
import json
import datetime

# Flask imports
from flask import request, Response, jsonify, Flask
from flask_restful import Resource, Api

from .Card import Card
from .Deck import Deck

class dealOneCard(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    def get(self):

        return "bye", 200

class shuffle(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    def get(self):

        return "hey", 200

app = Flask(__name__)
api = Api(app)

api.add_resource(shuffle, '/shuffle')
api.add_resource(dealOneCard, '/dealOneCard')

if __name__ == '__main__':
    app.run(debug=True)
