import random
from card import Card

# Class for a deck of cards, consisting of Card objects, methods include: build, shuffle, deal
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # resets/builds the deck completely anew when called
    def build(self):
        self.cards = []
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for value in values:
            for suit in suits:
                card = Card(suit, value)
                self.cards.append(card.__dict__)

    # shuffles deck
    def shuffle(self):

        self.build()

        # Implementing Fisher-Yates Shuffle Algorithm
        for i in range(len(self.cards)-1, 0, -1):
            j = random.randint(0, i+1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # deals top card
    def deal(self):
        return self.cards.pop()

    # converts deck to string for ease of use
    def __str__(self):
        deck_values = "\n"
        new_line = '\n'
        for card in self.cards:
            deck_values += f'{card}{new_line}'
        return f'The deck has:{deck_values}'