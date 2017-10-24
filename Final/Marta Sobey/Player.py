

class Player(object):
	"""This class is going to give each player a name and an empty list of cards.
		It will also add cards from the deck to each player's empty list."""
	def __init__ (self, name):
		self.name = name
		self.cardlist = []
		
	def add(self, deck):
		self.cardlist.append(deck)