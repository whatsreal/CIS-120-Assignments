#Brian Jansen
#Final Project - Codename: PokeHerFace

import os
import os.path
import operator
from player import *
from npc import *
from card import *
from deck import *
from table import *
from random import shuffle, randint, choice
from sys import exit
from collections import Counter

def startgame(name, phase, cash, count):
	"""This function prepares all the objects neccesary to start the game, and then calls the game() function."""
	dasdeck = deck()
	dastable = table(dasdeck)
	mainplayer = player(name,cash)
	dastable.addplayer(mainplayer, cash)
	if phase == "new":
		dastable.populatetable(dasdeck,count,mainplayer)
	game(dastable,mainplayer,dasdeck)

def resumegame():
	"""This is the function used to resume a game after it has been loaded using the reloadtable() function in the "table" object."""
	dasdeck = deck()
	dastable = table(dasdeck)
	playname, playcash = dastable.reloadtable()
	mainplayer = player(playname, playcash)
	dastable.addplayer(mainplayer, playcash)
	table.flop = {}
	for i in dastable.playerlist.keys():
		dastable.playerlist[i].fold = False
		dastable.playerlist[i].hand = {}
	game(dastable,mainplayer,dasdeck)


def resetgame(table,player):
	"""This is the function that is used to reset everything in between hands.  It also includes a check to show whether the player wins or loses and acts appropriately."""
	os.system('cls' if os.name == 'nt' else 'clear')
	if player.cash > 10:
		dasdeck = deck()
		table.deck = dasdeck
		table.flop = {}
		for i in table.playerlist.keys():
			table.playerlist[i].fold = False
			table.playerlist[i].hand = {}
			if table.playerlist[i].cash < 10 and table.playerlist[i].npc == True:
				del table.playerlist[i]
		if len(table.playerlist.keys()) > 1:
			game(table,player,dasdeck)
		else:
			print "Congratulations, you won against the computer players!"
			addwinner(player.name)
			raw_input("Press Enter to Continue...")
			mainmenu("main")

	else:
		print "Sorry, you have no cash left"
		raw_input("Press Enter to Continue...")
		mainmenu("main")

def game(table,player,deck):
	"""This is the actual game function that loops through the proccess of a hand of poker"""
	phaselist = ["deal", "flop", "turn", "river", "show"]
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
				player.foldphase = phase
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
			print "The Flop was:"
			for i in flop.keys():
				print deck.deckdict[i].name
			print "\n"
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
				print winnerstuff
				print "Draw - No one wins..."
			cont = False
			print "Your pot is now %d" % player.cash
			cont = raw_input("\nWould you like to continue?  (Y(or Enter)\N)\n>> ").lower()
			if cont == "n":
				table.savetable(player)
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






def mainmenu(area):
	"""This is the function that displays the main menu, and parses the user's input"""
	string = False
	os.system('cls' if os.name == 'nt' else 'clear')
	if area == "main":
		print "Welcome to the Sin Simulator, Texas Holdem Poker!"
		print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
		print "Play"
		print "Hall of Fame"
#		print "Tutorial"
		print "Rules"
		print "Help"
		print "Exit"
		print "\n=-=-=-=-=-=-=-=-=-=\nWhat would you like to do?\n"
	while not string:
		string = raw_input(">> ").lower()
	os.system('cls' if os.name == 'nt' else 'clear')
	if string == "play":
		if os.path.isfile("save.pf"):
			playmenu("main")
		else:
			playmenu("new")
	elif string == "hall of fame":
		winlist()
	elif string == "tutorial":
		launchtut()
	elif string == "rules":
		rulemenu()
	elif string == "help":
		helpmenu()
	elif string == "exit":
		exit()
	else:
		mainmenu("main")

def helpmenu():
	"""This function simply displays some navigational help and some simple help for playing the game."""
	print "Help Menu"
	print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
	print """While navigating through the menus, just type what you would like to do.
For example, if "Play" is offered as an option, then typing "play"
(upper or lower case) will call that option.
	\nIn game, you can type either "call" to call, or you can simply press the
"Enter" key.  Alternatively, you can type "fold" to fold.  If you decide to
not continue after a hand, it will save thegame automatically, and you can
resume later. You also have the choice to start a new game within the "Play" menu.
	\nHope you enjoy the game!
	"""
	raw_input("\nPress Enter to return to the Main Menu...")
	mainmenu("main")

def rulemenu():
	"""This function just pulls up a wikipedia article for help since you said yourself 'If you can get it to pull up a webpage, I'll accept it.  ;)"""
	os.startfile("help.url")
	mainmenu("main")

def winlist():
	"""Pulls up the "Hall of Fame" which is my answer to the high score list.  The way the game is designed, winning is quite difficult."""
	print "Hall of Fame"
	print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
	filename = "winlist.pf"
	f = open(filename)
	for i in f:
		i = i.replace(";"," ")
		print i
	print "\nAll of these folks won against the computer.  Latest winner at the top."
	raw_input("\nPress Enter to return to the Main Menu...")
	mainmenu("main")

def addwinner(name):
	"""This function adds a winner to the list of winners in \"winlist.pf\""""
	savestring = "%s\n" % name.replace(" ",";")
	filename = "winlist.pf"
	f = open(filename, "r")
	for i in f:
		savestring += "%s" % i
	f = open(filename, "w")
	f.write(savestring)
	f.close()


def playmenu(area):
	"""This is the play menu.  It asks user input, and depending if they start a new game, or resume, it calls other functions and puts the game in motion"""
	string = False
	playername = False
	playerpass = False
	if area == "main":
		print "Play Menu"
		print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
		print "New Game"
		print "Resume Game"
		print "Go to Main Menu (Type Main Menu)"
		while not string:
			string = raw_input("\n=-=-=-=-=-=-=-=-=-=\nWhat would you like to do?\n>> ").lower()
		os.system('cls' if os.name == 'nt' else 'clear')
		deconstruct = string.split()
		if string == "new game" or deconstruct[0] == "new":
			playmenu("new")
		elif string == "resume game" or deconstruct[0] == "resume":
			resumegame()
		elif string == "main menu":
			mainmenu("main")
		else:
			playmenu("main")
	elif area == "new":
		number = False
		npccount = False
		success = False
		npccount = 0
		while not playername:
			playername = raw_input("What is your name?\n>> ")
		while not success:
			npccount = raw_input("How many computer players? (1-6)\n>> ")
			success = npccount.isdigit()
		npccount = int(npccount)
		if  npccount > 0 and npccount < 7:
			startgame(playername, "new", False, npccount)
		else:
			print "Please choose a number in the range of 1-6."
			raw_input("\nPress Enter to continue...")
			os.system('cls' if os.name == 'nt' else 'clear')
			playmenu("new")

mainmenu("main")
