from player import *
from pokerdecisions import *
from random import randint

class computerPlayer(player):
    """This is the computer player additions to player.
       Add two decision making functions:
       keepOrDraw -- decides what cards to keep.
       foldOrContinue -- decides whether to continue or not."""

    def __init__(self):
        possNames = ["George", "Tom", "Brenda", "Aimee", "Matt", "Hank", "Bear", "Doug", "Anna"]
        self.name = possNames[randint(0, 8)]
        self.hand = []
        self.score = 0

    def keepOrDraw(self):
        """Stupid simple decision tree.
           Keep cards if they form at least 3/4 of a hand."""
        keep = [] #list of card indeces to keep
        #Partial Straight Flush
        index = pair(self.hand)
        if index > 0:
            keep = [index -1, index]
            if additionalMatch(self.hand, index):
                keep.append(index+1)
                if additionalMatch(self.hand, index+1):
                    keep.append(index+2)
                elif FullHouse(self.hand, index):
                    keep = [0,1,2,3,4]
            elif pair(self.hand, index+1) > 0:
                if FullHouse(self.hand, index):
                    keep = [0,1,2,3,4]
                else:
                    ind2 = pair(self.hand, index+1)
                    keep.append(ind2)
                    keep.append(ind2-1)
        else:
            strIdx = self._smallStraight()
            if strIdx != 0:
                keep = strIdx
            flIdx = self._smallFlush()
            if flIdx != 0:
                keep = flIdx
        for i in range(4, 0, -1):
            if i not in keep:
                self.removeCard(i)

    def _smallStraight(self):
        for i in range(0, 3):
            if straight(self.hand[i:i+2]):
                return [i, i+1, i+2]
        return 0

    def _smallFlush(self):
        for i in range(0,3):
            if straight(self.hand[i:i+2]):
                return [i, i+1, i+2]
        return 0


    def foldorCont(self):
        """Return true if the hand is good enough to keep going.
           return false otherwise."""
        bestHand = handDecision(self.hand)
        if handRankings[bestHand] >= 2:
            return True
        return False
