from card import *
from random import shuffle
class deck(object):
    """This creates the deck of cards that we use to deal out cards to the player hands.
       The main attribute is a list of card objects.
       Besides the init function there are also deal and shuffle functions.
       I create the deck in the __init__ function."""

    def __init__(self):
        self.cardList = []
        for i in ['Hearts',  'Spades', 'Clubs', 'Diamonds']:
            for j in range(1, 14):
                self.cardList.append(card(j, i))

    def shuffle(self):
        shuffle(self.cardList)

    def deal(self):
        return self.cardList.pop()


mydeck = deck()
