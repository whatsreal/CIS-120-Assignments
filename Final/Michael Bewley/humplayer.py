from deck1 import *
from collections import defaultdict

class human_player(object):
	def __init__(self):
		self.hand = defaultdict(str)
		self.book = []
		self.score = 0
		self.name = raw_input("What is your name? ")
		
	def Draw(self, carddrawn):#adds card to hand
		if str(carddrawn) in self.hand:
			self.hand[str(carddrawn)] += 1
			self.checkForBooks()
		else:
			self.hand[str(carddrawn)] = 1
		
	def emptyCheck(self):
		if len(self.hand)==0: #checks if deck/hand is empty
			self.Draw()
	
	def checkForBooks(self): #Checks to see if you have four of the same card in your hand
		for key,val in self.hand.items(): 
			if val == 4: 
				self.book.append(key)
				print '%s completed the book of %s\'s.' % (self.name,key)
				self.score += 1
				del self.hand[key]
		self.emptyCheck()
	
	def fishFor(self,cards): #if card in hand, returns count and removes the card from hand
		if cards in self.hand:
			val = self.hand.pop(cards)
			self.emptyCheck()
			return val
		else: 
			return False

	def displayHand(self): 
		return ' '.join(key for key,val in self.hand.iteritems()
			for i in range(val))
		
				
	