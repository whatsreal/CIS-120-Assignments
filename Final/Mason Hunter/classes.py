#Mason Hunter CIS 120 classes
from random import randint
class human_player(object):
    def __init__(self):
        self.name = ""
        self.hand = []
        self.hand_score = 0
        self.winnings = 5
    def hit(self):
        x = randint(0,52)
        card = dealer.deck[x]
        del dealer.deck[x]
        self.hand.append(card)
        self.hand_score = self.hand_score + card[1]
        if self.hand_score > 21:
            self.hand_score = 0        
        print self.hand, self.hand_score
        return self.hand, self.hand_score
    def sit(self):
        return self.hand, self.hand_score
    def wager(self, bet):
        self.wager = bet
        self.winnings = self.winnings - self.wager
        return self.winnings, self.wager 

zzz = human_player()

class dealer(object):
    def __init__(self):
        self.deck = [("Two of Hearts",2),("Three of Hearts",3),("Four of Hearts",4),("Five of Hearts",5),("Six of Hearts",6),("Seven of Hearts",7),("Eight of Hearts",8),("Nine of Hearts",9),("Ten of Hearts",10),("Jack of Hearts",10),("Queen of Hearts",10),("King of Hearts",10),("Ace of Hearts", 99),("Two of Diamonds",2),("Three of Dimonds",3),("Four of Diamonds",4),("Five of Diamonds",5),("Six of Diamonds",6),("Seven of Diamonds",7),("Eight of Diamonds",8),("Nine of Diamonds",9),("Ten of Diamonds",10),("Jack of Diamonds",10),("Queen of Diamonds",10),("King of Diamonds",10),("Ace of Diamonds",99),("Two of Clubs",2),("Three of Clubs",3),("Four of Clubs",4),("Five of Clubs",5),("Six of Clubs",6),("Seven of Clubs",7),("Eight of Clubs",8),("Nine of Clubs",9),("Ten of Clubs",10),("Jack of Clubs",10),("Queen of Clubs",10),("King of Clubs",10),("Ace of Clubs",99),("Two of Spades",2),("Three of Spades",3),("Four of Spades",4),("Five of Spades",5),("Six of Spades",6),("Seven of Spades",7),("Eight of Spades",8),("Nine of Spades",9),("Ten of Spades",10),("Jack of Spades",10),("Queen of Spades",10),("King of Spades",10),("Ace of Spades",99)]

    def pot():
        pot == zzz.wager + cowboy.wager + gent.wager + prep.wager
        return pot
    def repopulate_deck(self):
        self.deck = [("Two of Hearts",2),("Three of Hearts",3),("Four of Hearts",4),("Five of Hearts",5),("Six of Hearts",6),("Seven of Hearts",7),("Eight of Hearts",8),("Nine of Hearts",9),("Ten of Hearts",10),("Jack of Hearts",10),("Queen of Hearts",10),("King of Hearts",10),("Ace of Hearts", 99),("Two of Diamonds",2),("Three of Dimonds",3),("Four of Diamonds",4),("Five of Diamonds",5),("Six of Diamonds",6),("Seven of Diamonds",7),("Eight of Diamonds",8),("Nine of Diamonds",9),("Ten of Diamonds",10),("Jack of Diamonds",10),("Queen of Diamonds",10),("King of Diamonds",10),("Ace of Diamonds",99),("Two of Clubs",2),("Three of Clubs",3),("Four of Clubs",4),("Five of Clubs",5),("Six of Clubs",6),("Seven of Clubs",7),("Eight of Clubs",8),("Nine of Clubs",9),("Ten of Clubs",10),("Jack of Clubs",10),("Queen of Clubs",10),("King of Clubs",10),("Ace of Clubs",99),("Two of Spades",2),("Three of Spades",3),("Four of Spades",4),("Five of Spades",5),("Six of Spades",6),("Seven of Spades",7),("Eight of Spades",8),("Nine of Spades",9),("Ten of Spades",10),("Jack of Spades",10),("Queen of Spades",10),("King of Spades",10),("Ace of Spades",99)]
        return self.deck
    def determine_winner(self):
        scores = [zzz.hand_score, gent.hand_score, cowboy.hand_score, prep.hand_score]
        win = max(scores)
        while len(scores) > 1:
            for i in scores:
                if i != win:
                    scores.remove(i)
                
        if scores[0] == zzz.hand_score:
            zzz.winnings = zzz.winnings + pot
        elif scores[0] == gent.hand_score:
            gent.winnings = gent.winnings + pot
        elif scores[0] == cowboy.hand_score:
            cowboy.winnings = cowboy.winnings + pot
        elif scores[0} == prep.handscore:
            prep.winnings = prep.winnings + pot
        return zzz.winnings, gent.winnings, cowboy.winnings, prep.winnings
                
                
        
      
dealer = dealer()

class computer_player(object):
    
    def __init__(self):
        self.name = ""
        self.threshold = 0
        self.hand = []
        self.hand_score = 0
        self.winnings = 5
        self.quips = []
        self.wager = 0
    def hit(self):
        x = randint(0,52)
        card = dealer.deck[x]
        del dealer.deck[x]
        self.hand.append(card)
        self.hand_score = self.hand_score + card[1]
        if self.hand_score > 21:
            self.hand_score = 0
        print self.hand, self.hand_score
        return self.hand, self.hand_score
    def sit(self):
        return self.hand, self.hand_score
    def wager(self):
        self.winnings = self.winnings - self.wager
        return self.winnings, self.wager
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
gent.wager = randint(0,gent.winnings)
gent.quips = ["Time will tell my friend, but remember: To the victor goes the spoils", "Some times the most popular choice is the wrong one"]
#Rooster Cogburn is the risky gamblin' cowboy
cowboy = computer_player()
cowboy.name = "Rooster Cogburn"
cowboy.hand = []
cowboy.winnings = 5
cowboy.wager = 1 + cowboy.winnings / 2
cowboy.hand_score = 0
cowboy.threshold = 17
cowboy.quips = ["No risk no reward","screw probabilities... I'm goin for it"]
#Eugene Forrester is the uptight preppy Ivy League know it all kid
prep = computer_player()
prep.name = "Eugene Forrester"
prep.threshold = 11
prep.hand = []
prep.hand_score = 0
prep.winnings = 5
prep.wager = prep.winnings / 5
prep.quips = ["Slow and steady wins the race", "Through mathematical reasoning I have determined another hit to be too risky a proposition"]    

zzz.hand_score = 16
cowboy.hand_score = 0
gent.hand_score = 18
prep.hand_score = 10
dealer.determine_winner()