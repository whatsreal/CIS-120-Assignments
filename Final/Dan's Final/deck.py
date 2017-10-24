from card import *
from random import shuffle
class deck(object):
    """This creates the deck of cards that we use to deal out cards to the player hands.
       The main attribute is a list of card objects.
       Besides the init function there are also deal and shuffle functions.
       I create the deck in the __init__ function."""

    def __init__(self):
        """Creates a list of cards.
           Populates the list with a standard deck of cards.
           Uses my Card class for cards."""

    def shuffle(self):
        """Shuffles the deck."""

    def deal(self):
        """Pops off the first card on the deck."""
