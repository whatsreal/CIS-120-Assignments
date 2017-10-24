from collections import defaultdict
import random
from random import randint
from deck1 import *

class comp_player(object):
	def __init__(self,name):
		self.name = name
		self.hand = defaultdict(str)
		self.book = []
		self.score = 0
        
	def Draw(self, carddrawn):#adds card to hand
		if str(carddrawn) in self.hand:
			self.hand[str(carddrawn)] += 1
			self.checkForBooks()
		else:
			self.hand[str(carddrawn)] = 1
			
	def emptyCheck(self):
		if len(self.hand)==0: #checks if deck/hand is empty
			self.Draw()
			
	def decisions(self): #Check to see if the computer ha the card that is is asking for
		check = [0,0]
		for key,val in self.hand.items():
			if val > check[1]:
				check = [key,val]
		return check[0]
	
	def fishFor(self, cards):
		if cards in self.hand: # if card in hand, returns count and removes the card from hand
			val = self.hand.pop(cards)
			self.emptyCheck()
			return val
		else: 
			return False

	def checkForBooks(self): #If there is four of the same card then 
		for key,val in self.hand.items(): 
			if val == 4: 
				self.book.append(key)
				self.score += 1
				del self.hand[key]
				
	def playchoice(self, numplayers): # Picks a random player to ask for a card
		r = random.randint(0, numplayers)
		return r