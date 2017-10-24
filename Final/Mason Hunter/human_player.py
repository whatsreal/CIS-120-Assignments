#Mason Hunter CIS 120 human user
from random import randint
from time import sleep
class human_player(object):
    def __init__(self):
        self.name = ""
        self.hand = []#the hand is a list of cards(and each card is a list of form [(card name), (card value)]
        self.hand_score = 0
        self.winnings = 5#everyone starts with 5 bucks

    def hit(self, card):
        """This function takes a card (which is dealt by the dealer) and puts it into
        the user's hand.  It recalculates their new hand and hand score, and if
        their new hand is over 21 it busts the user"""
        self.hand.append(card)
        self.hand_score = self.hand_score + card[1]
        if self.hand_score > 21:
            print "BUSTED SUCKAH!", self.hand
            sleep(1)#this just gives the user a second to read their new hand and learn their fate before moving to the scoreboard
            return False, self.hand, self.hand_score
        print self.hand
        return self.hand, self.hand_score
    def sit(self):
        """This function just sits on their hand, basically passes the hand through"""
        return self.hand, self.hand_score
    def gamble(self, wager):
        """After the user makes a wager, this function subtracts that wager from their winnings"""
        self.winnings = self.winnings - wager
        return self.winnings
    def score(self, card):
        """Basically, this function is just in case the user draws an ace,
        and it gives the user the option of having the ace count for 1 or 10"""
        if card[1] == 99:
            print card
            turtle = 0#this turtle variable is just so that the while loop will continue until the user inputs a valid integer
            while turtle != 5:           
                try:
                    x = input("Would you like that Ace to be a 1 or a 10? > ")
                    turtle = 5
                except NameError:
                    print "That was not an integer\n"
                    turtle = 0
            if x == 1:
                pass
            elif x == 10:
                pass
            else:#if the user tries to get tricky and make an ace count for something other than 1 or 10 they get kicked out of the casino    
                print "You dirty cheater, get out of here and don't come back!!!"
                return False
            card[1] = x
        return card
