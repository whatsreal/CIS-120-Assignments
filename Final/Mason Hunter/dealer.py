from random import randint
class dealer(object):
    def __init__(self):
        self.deck = [["Two of Hearts",2],["Three of Hearts",3],["Four of Hearts",4],["Five of Hearts",5],["Six of Hearts",6],["Seven of Hearts",7],["Eight of Hearts",8],["Nine of Hearts",9],["Ten of Hearts",10],["Jack of Hearts",10],["Queen of Hearts",10],["King of Hearts",10],["Ace of Hearts", 99],["Two of Diamonds",2],["Three of Diamonds",3],["Four of Diamonds",4],["Five of Diamonds",5],["Six of Diamonds",6],["Seven of Diamonds",7],["Eight of Diamonds",8],["Nine of Diamonds",9],["Ten of Diamonds",10],["Jack of Diamonds",10],["Queen of Diamonds",10],["King of Diamonds",10],["Ace of Diamonds",99],["Two of Clubs",2],["Three of Clubs",3],["Four of Clubs",4],["Five of Clubs",5],["Six of Clubs",6],["Seven of Clubs",7],["Eight of Clubs",8],["Nine of Clubs",9],["Ten of Clubs",10],["Jack of Clubs",10],["Queen of Clubs",10],["King of Clubs",10],["Ace of Clubs",99],["Two of Spades",2],["Three of Spades",3],["Four of Spades",4],["Five of Spades",5],["Six of Spades",6],["Seven of Spades",7],["Eight of Spades",8],["Nine of Spades",9],["Ten of Spades",10],["Jack of Spades",10],["Queen of Spades",10],["King of Spades",10],["Ace of Spades",99]]
        #the deck is a list of cards(and each card is a list of form [(card name), (card value)]
    def deal(self):
        """This function deals two cards to each player"""
        x = randint(0,len(self.deck) - 1)#a random numbered card from the deck
        X = self.deck[x]#picking out that random card
        del self.deck[x]#eliminating that card
        y = randint(0,len(self.deck) - 1)
        Y = self.deck[y]
        del self.deck[y]
        return [X,Y]#returns a hand of two cards
    def deal_a_hit(self):
        """Deals a card to a player"""
        x = randint(0,len(self.deck) - 1)
        card = self.deck[x]
        del self.deck[x]
        return card
    def repopulate_deck(self):# I didn't end up using this function, as I simply re-instantiated the Bernie_Mac object which re-instantiated the deck
        """At the end of the round it puts the shuffled cards back in the deck"""
        self.deck = [["Two of Hearts",2],["Three of Hearts",3],["Four of Hearts",4],["Five of Hearts",5],["Six of Hearts",6],["Seven of Hearts",7],["Eight of Hearts",8],["Nine of Hearts",9],["Ten of Hearts",10],["Jack of Hearts",10],["Queen of Hearts",10],["King of Hearts",10],["Ace of Hearts", 99],["Two of Diamonds",2],["Three of Diamonds",3],["Four of Diamonds",4],["Five of Diamonds",5],["Six of Diamonds",6],["Seven of Diamonds",7],["Eight of Diamonds",8],["Nine of Diamonds",9],["Ten of Diamonds",10],["Jack of Diamonds",10],["Queen of Diamonds",10],["King of Diamonds",10],["Ace of Diamonds",99],["Two of Clubs",2],["Three of Clubs",3],["Four of Clubs",4],["Five of Clubs",5],["Six of Clubs",6],["Seven of Clubs",7],["Eight of Clubs",8],["Nine of Clubs",9],["Ten of Clubs",10],["Jack of Clubs",10],["Queen of Clubs",10],["King of Clubs",10],["Ace of Clubs",99],["Two of Spades",2],["Three of Spades",3],["Four of Spades",4],["Five of Spades",5],["Six of Spades",6],["Seven of Spades",7],["Eight of Spades",8],["Nine of Spades",9],["Ten of Spades",10],["Jack of Spades",10],["Queen of Spades",10],["King of Spades",10],["Ace of Spades",99]]
        return self.deck
    def determine_winner(self, hand1, hand2, hand3, hand4):
        """Takes as  arguments the hands of each player and then determines the winner
        Outputs a list the winning score (or scores)"""
        scores = [hand1, hand2, hand3, hand4]
        f_scores = []
        while len(scores) > 0:
            x = scores.pop()#pops off one score at a time. If it is greater than 21 it deletes it.  If under 21 adds to a list of eligible scores (f.scores)
            if x > 21:
               pass
            else:
                f_scores.append(x)
        win = max(f_scores)#this is the highest score which is under 21
        while len(f_scores) > 0:
            y = f_scores.pop()#pops off one eligible score at a time and then appends the winning score(s) to list scores
            if y == win:
                scores.append(y)
        return scores

    def score(self, hand):
        """This function checks a CPU's hand to see if it was dealt any aces.  If it was, the CPU "decides" whether it should be a 1 or 10"""
        hand_score = 0
        for i in hand:
           if i[1] == 99:
               hand.append(i)
               del hand[0]
               break
        for i in hand:#the CPU takes the ace as a 10 if their hand score is between 9 and 11, and if it's not the ace equals a 1
            if i[1] == 99:
                if hand_score < 12 and hand_score > 8:
                    i[1] = 10
                else:
                    i[1] = 1
            hand_score = hand_score + i[1]

        return hand_score


Bernie_Mac = dealer()#Bernie Mac played a BlackJack dealer in 'Ocean's 11'
