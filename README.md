# Medsender Internship Project
This project was assigned to be completed as a task for an intership from Medsender
The goal of the project was to create an api with a few different endpoints

## About the Project:
Create an api to reflect a deck of cards

## Endpoints:
shuffle - Shuffle returns returns a deck of cards in random order. Please do not use library-provided “shuffle” operations to implement this function. You may use library provided random number generators in your solution if needed.

dealOneCard - This function should return one card from the deck to the caller. Specifically, a call to shuffle followed by 52 calls to dealOneCard should result in the caller being provided all 52 cards of the deck in a random order. If the caller then makes a 53rd call dealOneCard, no card is dealt.

reset/build - This functions creates the deck anew once a deck has been shuffled or cards have been all dealth
