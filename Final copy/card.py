class card(object):
    """Defines the basic card class.
       Card is made of a rank and suit attribute.
       Card can output a string of form '<rank> of <suit>'"""

    def __init__(self, nRank, nSuit):
        self.rank = nRank
        self.suit = nSuit

    def outputCard(self):
        myStr = ""
        if self.rank == 1:
            myStr += "Ace "
        elif self.rank == 11:
            myStr += "Jack "
        elif self.rank == 12:
            myStr += "Queen "
        elif self.rank == 13:
            myStr += "King "
        else:
            myStr += str(self.rank) + " "

        return myStr + "of " + self.suit
