import random


class card_deck(object):
    def __init__(self):
        self.cards = []
        self.rank = 0
        rank_name=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
#for loop for suit and name
        for i in range(4):
            for k in rank_name:
                self.cards.append([k])
    def value(self):
        if self.rank == 'Ace':
             return 1
        elif self.rank == 'Jack':
             return 11
        elif self.rank == 'Queen':
             return 12
        elif self.rank == 'King':
             return 13
             
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()