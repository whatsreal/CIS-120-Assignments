#Player Class
from collections import Counter

class player(object):
	"""This is the class for the players of the game, both human and computer."""
	def __init__(self, name, cash):
		"""Instantiates the class and sets the variables."""
		self.name = name
		if not cash:
			self.cash = 100
		else:
			self.cash = cash
		self.blind = False
		self.npc = False
		self.dealer = False
		self.fold = False
		self.hand = {}

	def receivecards(self,cardlist):
		"""Really simple function to set the player's "hand" variable as a list."""
		self.hand = cardlist

	def calchand(self,deck,flop,phase):
		"""This function contains various algorithms that returns a dictionary that says what variations of poker hands that each player has."""
		handstats = {}
		combhandnum = []
		combhandabb = []
		handstats["straight"] = False
		handstats["flush"] = False
		handstats["fullhouse"] = False
		handstats["twokind"] = False
		handstats["threekind"] = False
		handstats["fourkind"] = False
		handstats["twopair"] = False
		handstats["pocketdouble"] = False
		handstats["straightflush"] = False
		handstats["highcard"] = 0
		handstats["highsuit"] = 0
		handstats["highstreak"] = 0
	#	print self.hand.keys()
		for i in self.hand.values(),flop.values():
			for p in i:
				combhandnum.append(int(p))
		for i in self.hand.keys(),flop.keys():
			for p in i:
				combhandabb.append(p)
		combhandnum.sort()
		combhandabb.sort()


		##Pocket Doubles Check##
		if self.hand.values()[0] == self.hand.values()[1]:
			handstats["pocketdouble"] = True

		##High Card Check##
		highcardlist = []
		for i in self.hand.values():
			highcardlist.append(i)
		highcardlist.sort()
		handstats["highcard"] = highcardlist[1]
		##Straight Check Algorithm##
		combhandlist = []
		count = 0
		streak = 1
		for i in combhandnum:
			if i not in combhandlist:
				combhandlist.append(i)
		for i in combhandlist:
			if count > 0:
				before = count-1
				if int(i) == int(combhandlist[before])+1:
					streak += 1
				else:
					streak == 1
			count += 1
		if streak >= 5:
			handstats["straight"] = True
		handstats["highstreak"] = streak
		##Flush Check Algorithm##
		count = 0
		highsuit = 0
		suitlist = []
		for i in combhandabb:
			suitlist.append(deck.deckdict[i].suit)
		suitcount = Counter(suitlist)
		for i in suitcount.values():
			if i > highsuit:
				highsuit = i
			if i == 5:
				#Flush
				handstats["flush"] = True
				if handstats["straight"] == True:
					#Straight Flush
					handstats["straighflush"] = True
		handstats["highsuit"] = highsuit

		##Pair and Full House Check Algorithm##
		count = 0
		threecount = 0
		handcount = Counter(combhandnum)
		for i in handcount.values():
			if i == 4:
				#Four of a Kind
				handstats["fourkind"] = True
			elif i == 3:
				#Three of a Kind
				threecount += 1
				handstats["threekind"] = True
				if threecount == 2:
					#Full House
					handstats["fullhouse"] = True
			elif i == 2:
				count += 1
				if count < 2 and handstats["threekind"] == False and handstats["fourkind"] == False:
					#Two of a Kind (One Pair)
					handstats["twokind"] = True
				if count == 2:
					#Two Pair
					handstats["twopair"] = True
					handstats["twokind"] = False
					if handstats["threekind"] == True:
						#Full House
{}						handstats["fullhouse"] = True
		self.handstat = handstats
		return handstats
