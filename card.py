import random

# Card class used for representing a playing card with a value and suit fields
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # tostring converting method for the object
    def __str__(self):
        return f"{self.value} of {self.suit}"