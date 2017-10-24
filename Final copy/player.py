class player(object):
    """This creates our player for the game.
       This player has a hand of cards, a name and a score.
       There is no function except init."""

    def __init__(self, pName):
        self.name = pName
        self.hand = []
        self.score = 0

    def removeCard(self, cIndex):
        """Takes the index of the card to remove.
           Removes a card from the hand and returns it."""
        rCard = self.hand[cIndex]
        del self.hand[cIndex]
        return rCard

    def addCard(self, cToAdd):
        self.hand.append(cToAdd)


    def sortHand(self):
        for i in range(0, len(self.hand)):
            for j in range(i+1, len(self.hand)):
                if self.hand[i].rank > self.hand[j].rank:
                    self.hand[i], self.hand[j] = self.hand[j], self.hand[i]
