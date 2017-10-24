#Table Class

from random import shuffle
from npc import * 

class table(object):
	"""This table class is essentially a variable manager that stands as a middle-man between other classes."""
	def __init__(self,deck):
		"""Instantiates the table instance with a bunch of variables.  Some useless."""
		self.deck = deck
		self.smallblind = 5
		self.bigblind = 10
		self.startingcash = 100
		self.playerlist = {}
		self.flop = {}		
		
	def addplayer(self, player, cash):
		"""Adds a player to the table's player list."""
		self.playerlist[player.name] = player
		if not cash:
			player.cash = self.startingcash
		else:
			player.cash = cash
		
	def populatetable(self,deck,npccount,player):
		"""Read's names from the names file from Project Euler, and then creates a specified number of npc's for the human player to play against."""
		namefl = "names.pf"
		namefile = open(namefl)
		nametext = namefile.read()
		namefile.close()
		nametext = nametext.replace('"', '')
		namelist = nametext.split(",")
		shuffle(namelist)
		count = 0
		for i in range(0,npccount):
			dup = True
			while dup == True:
				count += 1
				randname = namelist[count]
				if randname != player.name:
					dup = False
			self.playerlist[randname] = npc(randname,self,False,False,False,False)
				
	def reloadtable(self):
		"""Loads a saved game from save.pf and then populates the table according to the information provided."""
		splitlist = []
		play = False
		filename = "save.pf"
		f = open(filename)
		for i in f:
			splitlist = []
			for p in i.split():
				p = p.replace(";"," ")
				splitlist.append(p)
			if play: 
				self.playerlist[splitlist[0]] = npc(splitlist[0],self,int(splitlist[1]),False,False,False)
			else:
				playname = splitlist[0]
				playcash = int(splitlist[1])
				play = True
		f.close()
		return playname, playcash
		
	def savetable(self, player):
		"""Saves the game's information in "save.pf" so that the player can resume the game later."""
		savestring = "%s %s\n" % (player.name, player.cash)
		filename = "save.pf"
		for i in self.playerlist.keys():
			if self.playerlist[i].npc == True:
				icash = str(self.playerlist[i].cash)
				istring = i.replace(" ", ";")
				savestring += "%s %s\n" % (istring, icash)
		f = open(filename, "w")
		f.write(savestring)
		f.close()
				
	
	def deal(self, deck):
		"""Deals cards from the shuffled list to the player.  Called at the beginning of the round."""
		for i in self.playerlist.keys():
			if self.playerlist[i].fold == False:
				for p in range(0,2):
					card = deck.cardkeylist.pop()
					self.playerlist[i].hand[card] = deck.deckdict[card].numval
	
	def decidewinner(self, deck):
		"""Goes through the list of players who have not folded, and then returns who won, why, and whether there is a draw."""
		handname = {}
		handname["straight"] = "Straight"
		handname["flush"] = "Flush"
		handname["fullhouse"] = "Full House"
		handname["twokind"] = "Two of a Kind"
		handname["threekind"] = "Three of a Kind"
		handname["fourkind"] = "Four of a Kind"
		handname["twopair"] = "Two Pair"
		handname["pocketdouble"] = "Pocket Doubles"
		handname["straightflush"] = "Straight Flush"
		handname["highcard"] = "High Card"
		handrank = ["straightflush", "fourkind", "fullhouse", "flush", "straight", "threekind", "twopair", "twokind"]
		winlist = []
		victordict = {}
		winner = False
		draw = False
		for i in handrank:
			for p in self.playerlist.keys():
				if self.playerlist[p].handstat[i] == True and self.playerlist[p].fold == False:
					winlist.append(p)
					winner = True
					winninghand = i
			if winner == True:
				break
		highcard = 0
		if len(winlist) > 1:
			victor = False
			drawlist = []
			for i in winlist:
				if self.playerlist[i].handstat["highcard"] > highcard:
					highcard = self.playerlist[i].handstat["highcard"]
					victor = i
					draw = False
				elif self.playerlist[i].handstat["highcard"] == highcard:
					drawlist.append(i)
					draw = True
		elif len(winlist) == 0:
			victor = False
			drawlist = []
			for p in self.playerlist.keys():
				if self.playerlist[p].handstat["highcard"] > highcard:
					highcard = self.playerlist[p].handstat["highcard"]
					victor = p
					draw = False
					winninghand = "highcard"
				elif self.playerlist[p].handstat["highcard"] == highcard:
					drawlist.append(p)
					draw = True					
		else:
			victor = winlist[0]
		victordict["name"] = victor
		victordict["hand"] = handname[winninghand]
		victordict["highcard"] = highcard
		victordict["draw"] = draw
		return victordict

	def debugflop(self, deck):
		"""Little function I used early on before I added an interface to check other functions."""
		for i in range(0,5):
			card = deck.cardkeylist.pop()
			self.flop[card] = deck.deckdict[card].numval
		print self.flop
		return self.flop
		
	def burnturn(self,deck,phase,flop):
		"""In traditional poker fashion, this function "burns" a card and then "turns" a card onto the flop. Does this in a 3-1-1 fashion."""
		if phase == "flop":
			for i in range(0,4):
				if i > 0:
					card = deck.cardkeylist.pop()
					self.flop[card] = deck.deckdict[card].numval
		elif phase == "turn" or phase == "river":
			for i in range(0,2):
				if i > 0:
					card = deck.cardkeylist.pop()
					self.flop[card] = deck.deckdict[card].numval
		return self.flop
			
	def npcbetcall(self, flop, phase):
		"""This function goes through the list of NPCs and calls the calcmove() function to decide whether or not they will fold, and then acts accordingly."""
		foldlist = []
		inlist = []
		for i in self.playerlist.keys():
			if self.playerlist[i].npc == True and self.playerlist[i].fold == False:
				if self.playerlist[i].calcmove(self.deck,flop,phase) == "fold":
					foldlist.append(i)
					self.playerlist[i].fold = True
				else:
					inlist.append(i)
		return foldlist, inlist
