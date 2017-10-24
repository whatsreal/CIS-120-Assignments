#Deck Class

from random import shuffle
from card import *

class deck(object):
	"""This class is the class for the entire deck of cards.  More or less a glorified dictionary."""
	def __init__(self):
		"""Creates the instance and shuffles the 'Deck'"""
		self.shufflist = {}                             
		self.createdeck()
		keylist = self.abblist.keys()
		shuffle(keylist)
		self.cardkeylist = keylist
		for i in keylist:
			self.shufflist[i] = self.abblist[i]
		
	
	def createdeck(self):
		"""This function goes through the suits and creates the card for each suit and populates the deck."""
		decklist = {}
		abblist = {}
		count = 1
		for i in range(1,5):
			if i == 1:
				suit = "Hearts"
				suitabb = "h"
			elif i == 2:
				suit = "Spades"
				suitabb = "s"
			elif i == 3:
				suit = "Clubs"
				suitabb = "c"
			else:
				suit = "Diamonds"
				suitabb = "d"
			for p in range(2, 15):
				if p == 11:
					nameval = "Jack"
					nameabb = "j"
				elif p == 12:
					nameval = "Queen"
					nameabb = "q"
				elif p == 13:
					nameval = "King"
					nameabb = "k"
				elif p == 14:
					nameval = "Ace"
					nameabb = "a"
				else:
					nameval = p
					nameabb = str(p)
				name = "%s of %s" % (nameval, suit)
				dickt = nameabb + suitabb
				abblist[dickt] = p
				decklist[dickt] = card(suitabb,name,p,count)
				count += 1
		self.deckdict = decklist
		self.abblist = abblist
