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
    index = pair(handIn)
    if index > 0: #Pair True
        if additionalMatch(handIn, index): #Three of a Kind
            index += 1
            if additionalMatch(handIn, index): #Four of a Kind
                index += 1
                return "Four of a Kind"
            elif FullHouse(handIn, index):
                return "Full House"
            else:
                return "Three of a Kind"
        elif pair(handIn, index+1) > 0:
            if FullHouse(handIn, index):
                return "Full House"
            else:
                return "Two Pair"
        else:
            return "Pair"
    elif straight(handIn):
        if flush(handIn):
            return "Straight Flush"
        else:
            return "Straight"
    elif flush(handIn):
        return "Flush"
    else:
        return "High Card"


def pair(handIn, indx = 0):
    for i in range(indx, len(handIn)-1):
        if handIn[i].rank == handIn[i+1].rank:
                return i+1
    return -1


def additionalMatch(handIn, indx):
    if handIn[indx].rank == handIn[indx+1].rank:
        return True
    return False

def flush(handIn):
    for i in range(0, len(handIn)-1):
        if handIn[i].suit != handIn[i+1]:
            return False
    return True

def straight(handIn):
    for i in range(0, len(handIn)-1):
        if handIn[i].rank != (handIn[i+1].rank) - 1:
            return False
    return True

def FullHouse(handIn, indx):
    if indx == 2:
        if handIn[3].rank == handIn[4].rank:
            return True
    elif indx == 1:
        if handIn[2].rank == handIn[3].rank and handIn[2].rank == handIn[4].rank:
            return True
    return False
