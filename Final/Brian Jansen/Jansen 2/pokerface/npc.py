#Non Player Charecter Class

from player import *
from random import randint

class npc(player):
	"""This is the class for Non-Player Charecters.  It is also a type of the "player" class."""
	def __init__(self, name, table, cash, skill, intelligence, predictability):
		"""Instantiates the class and defines various variables."""
		super(npc, self).__init__(name,table)
		self.skill = skill
		self.intelligence = intelligence
		self.predictability = predictability
		if not cash:
			self.cash = table.startingcash
		else:
			self.cash = cash
		self.npc = True
	
	def calcmove(self, deck, flop, phase):
		"""This function is where the computer decides whether the NPC should "call" or "fold" based on it's hand."""
		foldhands = [[2, 7], [2, 8]]
		betcond = ["twopair", "threekind", "straight", "flush", "fullhouse", "fourkind", "straightflush"]
		maybecond = ["twokind"]
		if phase == "deal":
			if self.hand.values()[0] == self.hand.values()[1]:
				return "call"
			elif self.hand.values()[0] == self.hand.values()[1]-1:
				return "call"
			elif deck.deckdict[self.hand.keys()[0]].suit == deck.deckdict[self.hand.keys()[1]].suit:
				return "call"
			for i in foldhands:
				if i.sort() == self.hand.values().sort():
					return "fold"
			chance = randint(1,100)
			if chance > 75:
				return "fold"
			else:
				return "call"
				
		else:
			self.calchand(deck,flop,phase)
			chancea = randint(1,100)
			chanceb = randint(1,100)
			chancec = randint(1,100)
			chanced = randint(1,100)
			if phase == "flop":
				mincard = 2
				percmod = 90
				phasenum = 1
			elif phase == "turn":
				mincard = 3
				percmod = 70
				phasenum = 2
			elif phase == "river":
				mincard = 4
				percmod = 50
				phasenum = 3
			elif phase == "show":
				mincard = 3
				percmod = 45
				phasenum = 4
			for i in betcond:
				if self.handstat[i] == True:
					return "call"
			for i in maybecond:
				if self.handstat[i] == True:
					if chancea < percmod:
						return "call"
			if self.handstat["highsuit"] > mincard:
				if chanceb < percmod:
					return "call"
			if self.handstat["highstreak"] > mincard:
				if chancec < percmod:
					return "call"
			if chanced > percmod:
				return "fold"
			else:
				return "call"
