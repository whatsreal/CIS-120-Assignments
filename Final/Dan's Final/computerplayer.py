from player import *
from pokerdecisions import *
from random import randint

class computerPlayer(player):
    """This is the computer player additions to player.
       Add two decision making functions:
       keepOrDraw -- decides what cards to keep.
       foldOrContinue -- decides whether to continue or not."""

    def __init__(self):
        """Creates a player object.
           This __init__ overrides Player.___init__().
           Adds a name randomly from a list supplied here."""

    def keepOrDraw(self):
        """Stupid simple decision tree.
           Keep cards if they form at least 3/4 of a hand."""


    def _smallStraight(self):
        """Helper for keepOrDraw().  Checks for a straight of 3 cards."""

    def _smallFlush(self):
        """HElper for keepOrdraw().
           Checks for a 3 card flush. (Badly incidentally)"""


    def foldorCont(self):
        """Return true if the hand is good enough to keep going.
           return false otherwise."""
