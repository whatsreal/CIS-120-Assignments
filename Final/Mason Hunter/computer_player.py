
from random import randint
class computer_player(object):
    
    def __init__(self):
        self.name = ""
        self.threshold = 0#this is the gambling threshold, if their hand score is lower than this the CPU hits, if it's higher they sit
        self.hand = []#the hand is a list of cards(and each card is a list of form [(card name), (card value)]
        self.hand_score = 0
        self.winnings = 5#everybody starts with 5 bucks
        self.quips = []
        self.wager = 0
    def hit(self, card):
        """In this function the CPU gets passed a card from the dealer and then that
        card gets added to their hand.  If the hand is then over 21 the CPU gets busted"""
        self.hand.append(card)
        self.hand_score = self.hand_score + card[1]
        if self.hand_score > 21 and self.hand_score < 90:#this is because an ace has a beginning value of 99, so if this "and < 90" is not the CPU gets an ace the program erroneously prints busted-then the hand continues as usual
            print "BUSTED SUCKAH!", self.hand, "\n\n\n\n"
            return False, self.hand, self.hand_score
        print self.hand
        return self.hand, self.hand_score
    def sit(self):
        """This function just sits on the CPU hand and passes it through"""
        return self.hand_score
    def gamble(self, wager):
        """This function takes the argument of the CPU's wager and subtracts that wager from their winnings"""
        self.winnings = self.winnings - wager
        return self.winnings
#Here I create the CPU's and give them their characteristics
#Lord Havisham is the ultra smooth British poker player    
gent = computer_player()
gent.name = "Lord Havisham"
x = randint(0,10)# Lord Havisham isn't as predictable as others, so his threshold changes
if x == 3 or 5 or 7:
    gent.threshold = 16
else:
    gent.threshold = 14
gent.hand = []
gent.hand_score = 0
gent.winnings = 5
gent.wager = randint(0,gent.winnings)#he is unpredictable and so is his betting
gent.quips = ["Time will tell my friend, but remember: To the victor goes the spoils", "Sometimes the most popular choice is the wrong one","Fortune favors the bold, not the reckless"]
#Rooster Cogburn is the risky gamblin' cowboy
cowboy = computer_player()
cowboy.name = "Rooster Cogburn"
cowboy.hand = []
cowboy.winnings = 5
cowboy.wager = 1 + cowboy.winnings / 2#a risky gambling strategy
cowboy.hand_score = 0
cowboy.threshold = 17#a high and risky threshold
cowboy.quips = ["No risk no reward","Screw probabilities!", "I've got a hunch", "It's better to have loved and lost than to have never lost at all"]
#Eugene Forrester is the uptight preppy Ivy League know it all kid
prep = computer_player()
prep.name = "Eugene Forrester"
prep.threshold = 11#a low and conservative threshold
prep.hand = []
prep.hand_score = 0
prep.winnings = 5
prep.wager = prep.winnings / 5#a conservative gambling strategy
prep.quips = ["Slow and steady wins the race", "Through mathematical reasoning I have determined another hit to be too risky a proposition", "I know you are but what am I", "Oh yeah well... Your Mom!"]    


