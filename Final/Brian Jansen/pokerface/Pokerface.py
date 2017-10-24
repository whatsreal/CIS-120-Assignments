#Brian Jansen
#Final Project - Codename: PokeHerFace

import os
import os.path
import operator
from random import shuffle, randint, choice
from sys import exit
from collections import Counter

class card(object):
	def __init__(self, suit, name, numval, numid):
		self.suit = suit
		self.name = name
		self.numval = numval
		self.numid = numid
		if suit is "s" or suit is "c":
			self.color = "b"
		else:
			self.color = "r"		
		
	
class deck(object):
	def __init__(self):
		self.shufflist = {}
		self.createdeck()
		keylist = self.abblist.keys()
		shuffle(keylist)
		self.cardkeylist = keylist
		for i in keylist:
			self.shufflist[i] = self.abblist[i]
		
	
	def createdeck(self):
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
#					nameabb = "%02d" % p
				name = "%s of %s" % (nameval, suit)
				dickt = nameabb + suitabb
				abblist[dickt] = p
				decklist[dickt] = card(suitabb,name,p,count)
#				print name, p, count, dickt
				count += 1
		self.deckdict = decklist
		self.abblist = abblist
	
class table(object):
	def __init__(self,deck,npccount,player):
		self.deck = deck
		self.smallblind = 5
		self.bigblind = 10
		self.startingcash = 100
		self.playerlist = {}
		self.flop = {}		
		
	def addplayer(self, player, cash):
		self.playerlist[player.name] = player
		if not cash:
			player.cash = self.startingcash
		else:
			player.cash = cash
		
	def populatetable(self,deck,npccount,player):
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
		
	def deal(self, deck):
		for i in self.playerlist.keys():
			for p in range(0,2):
				card = deck.cardkeylist.pop()
				self.playerlist[i].hand[card] = deck.deckdict[card].numval
	
	def decidewinner(self, deck):
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
		for i in range(0,5):
			card = deck.cardkeylist.pop()
			self.flop[card] = deck.deckdict[card].numval
		print self.flop
		return self.flop
		
	def burnturn(self,deck,phase,flop):
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
		
class player(object):
	def __init__(self, name, cash):
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
		self.hand = cardlist
		
	def calchand(self,deck,flop,phase):
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
						handstats["fullhouse"] = True
		self.handstat = handstats
		return handstats	
	
class npc(player):
	def __init__(self, name, table, cash, skill, intelligence, predictability):
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
				percmod = 40
				phasenum = 1
			elif phase == "turn":
				mincard = 3
				percmod = 30
				phasenum = 2
			elif phase == "river":
				mincard = 4
				percmod = 20
				phasenum = 3
			elif phase == "show":
				mincard = 3
				percmod = 15
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

def startgame(name, phase, cash):
	dasdeck = deck()
	mainplayer = player(name,cash)
	dastable = table(dasdeck,5,mainplayer)
	dastable.addplayer(mainplayer, cash)
	if phase == "new":
		dastable.populatetable(dasdeck,5,mainplayer)
	game(dastable,mainplayer,dasdeck)
	
def resetgame(table,player):
	os.system('cls' if os.name == 'nt' else 'clear')
	if player.cash > 10:
		dasdeck = deck()
		table.deck = dasdeck
		table.flop = {}
		for i in table.playerlist.keys():
			table.playerlist[i].fold = False
			if table.playerlist[i].cash < 10 and table.playerlist[i].npc == True:
				del table.playerlist[i]
		if len(table.playerlist.keys()) > 1:
			game(table,player,dasdeck)
		else: 
			print "Congratulations, you win!"
			raw_input("Press Enter to Continue...")
			mainmenu("main")
			
	else:
		print "Sorry, you have no cash left"
		raw_input("Press Enter to Continue...")
		mainmenu("main")
	
def game(table,player,deck):
	phaselist = ["deal", "flop", "turn", "river", "show"]
#	dasdeck = deck()
	table.deal(deck)
	flop = []
	for phase in phaselist:
		os.system('cls' if os.name == 'nt' else 'clear')
		if phase == "deal":
			print "[$%d]%s, your hand is:" % (player.cash, player.name)
			print deck.deckdict[player.hand.keys()[0]].name, "&", deck.deckdict[player.hand.keys()[1]].name
			if player.fold == False:
				print "\nWould you like to fold or call?"
				choice = raw_input(">> ")
			if choice == "fold":
				player.fold = True
			os.system('cls' if os.name == 'nt' else 'clear')
		elif phase == "show":
			foldlist, inlist = table.npcbetcall(flop, "show")
			player.calchand(deck, flop, phase)
			winnerstuff = table.decidewinner(deck)
			for p in table.playerlist.keys():
				if table.playerlist[p].fold == False:
					print "[$%d]%s's hand was:" % (table.playerlist[p].cash, table.playerlist[p].name)
					print deck.deckdict[table.playerlist[p].hand.keys()[0]].name, "&", deck.deckdict[table.playerlist[p].hand.keys()[1]].name
					print "\n"
					if winnerstuff["name"] != table.playerlist[p].name and winnerstuff["draw"] != True:
						table.playerlist[p].cash = table.playerlist[p].cash - 10
			if winnerstuff["draw"] != True:
				if winnerstuff["highcard"] != 0:
					if winnerstuff["highcard"] == 11: winnerstuff["highcard"] = "Jack"
					elif winnerstuff["highcard"] == 12: winnerstuff["highcard"] = "Queen"
					elif winnerstuff["highcard"] == 13: winnerstuff["highcard"] = "Kind"
					elif winnerstuff["highcard"] == 14: winnerstuff["highcard"] = "Ace"
					print "%s won the hand with a %s and a high card of %s" % (winnerstuff["name"], winnerstuff["hand"], winnerstuff["highcard"])
				else:
					print "%s won the hand with a %s" % (winnerstuff["name"], winnerstuff["hand"])
				table.playerlist[winnerstuff["name"]].cash += 10
			else:
				print "Draw - No one wins..."
			cont = False
			print "Your pot is now %d" % player.cash
			cont = raw_input("Would you like to continue?  (Y (or Enter)/N)\n>> ").lower()
			if cont == "n":
				mainmenu("main")
			else:
				resetgame(table,player)
				
		else:	
			flop = table.burnturn(deck, phase, flop)
			foldlist, inlist = table.npcbetcall(flop, phase)
			print " | ".join(inlist)
			print "\n"
			print "[$%d]%s, your hand is:" % (player.cash, player.name)
			print deck.deckdict[player.hand.keys()[0]].name, "&", deck.deckdict[player.hand.keys()[1]].name
			print "\n"
			foldstr = " | ".join(foldlist)
			print "%s folded" % foldlist
			print "\n"
			print "The Flop is:" 
			for i in flop.keys():
				print deck.deckdict[i].name
			if player.fold == False:
				print "\nWould you like to fold or call? (Call will cost 10)"
				choice = raw_input(">> ")
			if choice == "fold":
				player.fold = True
			os.system('cls' if os.name == 'nt' else 'clear')
			
	
	
		
		
		
def mainmenu(area):
	string = False
	os.system('cls' if os.name == 'nt' else 'clear')
	if area == "main":
		print "Welcome to the Sin Simulator, Texas Holdem Poker!\n"
		print "Play"
#		print "Tutorial"
#		print "Rules"
		print "Help"
		print "Exit"
	while not string:
		string = raw_input("\n=-=-=-=-=-=-=-=-=-=\nWhat would you like to do?\n>> ").lower()
	os.system('cls' if os.name == 'nt' else 'clear')
#	deconstruct = string.split()
	if string == "play":
		exist = True
		playername = False
		while not playername:# or exist:
			playername = raw_input("What is your name?\n>> ")
#			exist = exists(playername)
		startgame(playername, "new", False)
#	elif string == "tutorial":
#		launchtut()
#	elif string == "rules":
#		rulemenu()
	elif string == "help":
		helpmenu()
	elif string == "exit":
		exit()
	else:
		mainmenu("main")
		
def playmenu(area):
	global savelist
	string = False
	playername = False
	playerpass = False
	if area == "main":
		print "Play Menu\n"
		print "Start Game"
		print "Resume Game"
		print "Go to Main Menu (Type Main Menu)"
		while not string:
			string = raw_input("\n=-=-=-=-=-=-=-=-=-=\nWhat would you like to do?  (Type 'help' for a list of commands...)\n>> ").lower()
		os.system('cls' if os.name == 'nt' else 'clear')
		deconstruct = string.split()
		if string == "start game" or deconstruct[0] == "start":
			playmenu("start")
		elif string == "resume game" or deconstruct[0] == "resume":
			playmenu("resume")
		elif string == "main menu":
			mainmenu("main")
		else:
			playmenu("main")
	elif area == "start":
		exist = True
		while not playername or exist:
			playername = raw_input("What is your name?\n>> ")
			exist = exists(playername)
		startgame(playername, "new", False)
	elif area == "resume":
		exist = False
		while not playername and not exists:
			playername = raw_input("What is your name?\n>> ")
			exist = exists(playername)
		startgame(playername,"resume")
			
def loadplayers():
	global savelist
	conlist = []
	splitlist = []
	sortlist = []
	filename = "saves.pf"
	f = open(filename)
	for i in f:
		splitlist = []
		for p in i.split():
			p = p.replace(";"," ")
			splitlist.append(p)
		conlist.append(splitlist)
	f.close()
	savelist = conlist
	
def saveplayers():
	global savelist
	savestring = ""
	filename = "saves.pf"
	for i in savelist:
		for p in i:
			p = str(p)
			pstring = p.replace(" ", ";")
			savestring += "%s " % pstring
		savestring += "\n"	
	f = open(filename, "w")
	f.write(savestring)
	f.close()
	
def addsave(name,cash):
	"""This function is runs the user though the proccess of adding a contact's name, work place, and phone number and saves it to the external file at the end."""
	global savelist
	idlist = []
	for i in savelist:
		idlist.append(i[0])     
	randid = str(randint(1000,9999))
	while randid in idlist:
		randid = str(randint(1000,9999))
	newplayer = [randid, name, cash]
	savelist.append(newplayer)
	saveplayers()
	loadplayers()
	
def exists(name):
	global savelist
	exist = False
	namelist = []
	for i in savelist:
		namelist.append(i[1].lower())
	if name in namelist:
		return True
	else:
		return False

#dasdeck = deck()
#testguy = player("Testy",50)
#dastable = table(dasdeck,5,testguy
savelist = []
loadplayers()
#print savelist
mainmenu("main")


"""
Use a dictionary to act as a list for the cards
deck[2h] = card("h","Two of Hearts",2) 

deckvar.deck[2h].name = 
table.playerlist[name] = object

Letter Key
=-=-=-=-=-=
s = spades
h = hearts
d = diamonds
c = clubs
b = black
r = red
a = ace
k = king
qu = queen
j = joker
st = strait
roy = royal
fl = flush
fp = four of a kind
thp = three of a kind
twp = two pair
pd = pocket doubles
"""
