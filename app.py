# Standard python imports
import json
import datetime

# Flask imports
from flask import Flask
from flask_restful import Resource, Api

# Importing class Deck which consists of Card class objects
from deck import Deck
my_deck = Deck()


# Three endpoints for the api
class start(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    # reset endpoint at '/', restarts deck
    def get(self):
        try:
            my_deck.build()
            return "Deck Created", 200

        except:
            return "Error with reset", 400

class dealOneCard(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    # deal endpoint, deals one card from the top of the deck
    # does not deal if deck is empty
    def get(self):
        try:

            if my_deck.cards:
                # return str(my_deck.deal()), 200
                return json.dumps(my_deck.deal(), indent=2), 200

            return "No cards left in deck", 200

        except:
            return "Error with dealing", 400

class shuffle(Resource):
    
    # ===================
    #   GET METHOD
    # ===================

    # shuffle endpoint, allows for deck to be shuffled using the Fisher-Yates Algorithm
    def get(self):
        try:
            my_deck.shuffle()

            if my_deck.cards:
                # return str(my_deck), 200
                return json.dumps(my_deck.__dict__, indent=2), 200

            return "No cards left in deck", 200

        except: 
            return "Error with shuffling", 400

def create_app():

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(shuffle, '/shuffle')
    api.add_resource(dealOneCard, '/dealOneCard')
    api.add_resource(start, '/')

    return app

if __name__ == '__main__':

    app = create_app()
    app.run(port=5001)
