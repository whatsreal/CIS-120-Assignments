"""This is a collection of data on python hands to allow me to create a basic decision engine."""

handRankings = {"High Card":0,
                "Pair":1,
                "Two Pair":2,
                "Three of a Kind":3,
                "Straight":4,
                "Flush":5,
                "Full House":6,
                "Four of a Kind":7,
                "Straight Flush":8}

def handDecision(handIn):
    """Takes a hand, returns the best possible hand."""


def pair(handIn, indx = 0):
    """Takes a hand, looks for a pair.
       Assumes a sorted hand.
       Returns the index of the second card,
       or -1 if no pair is found."""

def additionalMatch(handIn, indx):
    """Checks for a card in the rest of the hand
       matching the one at position indx.
       returns true or false."""

def flush(handIn):
    """Looks for a flush.
       Returns True False.
       Assumes a sorted hand."""

def straight(handIn):
    """Checks for a straight in a hand.
       Returns True or False."""

def FullHouse(handIn, indx):
    """Checks for a fullhouse in the hand.
       Indx is either 1 or 2.  The cards after the index must all equal.
       Assume the cards before and up to the index
       match (ie passed pair() or additionalMatch())"""
