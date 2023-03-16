# Standard python imports
import json
import datetime

# Flask imports
from flask import Flask
from flask_restful import Resource, Api

from deck import Deck
my_deck = Deck()

class dealOneCard(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    def get(self):
        try:
            # return str(my_deck.deal()), 200
            # print(json.dumps(my_deck.deal().__dict__, indent=2))

            if my_deck.cards == []:
                return "No cards left in deck", 200

            return json.dumps(my_deck.deal().__dict__, indent=2), 200

        except:
            return "Error with dealing", 400

class shuffle(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    def get(self):
        try:
            my_deck.shuffle()
            if my_deck.cards == []:
                return "No cards left in deck", 200

            # return str(my_deck), 200
            return json.dumps(my_deck.__dict__, indent=2), 200

        except:
            return "Error with shuffle", 400

def create_app():

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(shuffle, '/shuffle')
    api.add_resource(dealOneCard, '/dealOneCard')

    return app

if __name__ == '__main__':

    app = create_app()
    app.run(debug=True)
