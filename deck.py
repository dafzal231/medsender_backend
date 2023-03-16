import random
from card import Card
import os


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for value in values:
            for suit in suits:
                card = Card(suit, value)
                self.cards.append(card)

    def shuffle(self):

        # Implementing Fisher-Yates Shuffle Algorithm

        for i in range(len(self.cards)-1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self):
        return self.cards.pop()

    def __str__(self):
        deck_values = ""
        new_line = '\n'
        for card in self.cards:
            deck_values += f'{card}{new_line}'
        return f'The deck has:{deck_values}'