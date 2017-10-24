#Michael Bewley
#Go Fish (Final Project)

import random
from sys import exit
from collections import defaultdict
from deck1 import *
from humplayer import *
from compplayer import *

save = "savegame.txt"

def Play():
	while True:
		compplay = input("How many computer players would you like? (2-4) ")

		hplay = human_player()
		numcomp = []
		x = ['Mike' , 'Betty' , 'Marta' , 'Steve']
		for i in range(0, compplay):
			player_name = random.choice(x)
			x.remove(player_name)
			newplayer = comp_player(player_name)
			numcomp.append(newplayer)
			global numcomp
			print "You will be playing against %s." % player_name

		mydeck = card_deck()
		mydeck.shuffle()

		for i in range(5):
                        print i
                        hplay.Draw(mydeck.deal())
			for i in numcomp:
				i.Draw(mydeck.deal())
				#return False
				#break

		check = True
		while check:
			if len(hplay.hand) == 0:
				check = False
				break
			print "\n\nYou have : "
			print "\t", hplay.displayHand(), "\n"
			n = raw_input("Who would you like to ask? ")
			for i in numcomp:
				if i.name == n:
					try:
						c = raw_input("What card would you like to ask for? ")
						for c in i.hand:
							hplay.fishFor(c)
							check = False
							for j in i.hand:
								hplay.Draw(mydeck.deal())
					except ValueError:
						print "I don't understand"
			for x in numcomp:
				k = x.playchoice(len(numcomp))
				h = x.decisions()
				if k == 0:
					for b in hplay.hand:
						if h[0] == b[0]:
							x.fishFor(b)
							check = False
							for j in hplay.hand:
								x.Draw(mydeck.deal())
				else:
					for b in numcomp[k-1].hand:
						if h[0] == b[0]:
							x.fishFor(b)
							check = False
							for j in numcomp[k-1].hand:
								x.Draw(mydeck.deal())
			if len(hplay.hand) == 0:
				check = False
				break

#def Save():
#	try:
#		sgame = raw_input("Are you sure you want to save and exit? (yes or no) "
#		if sgame == "yes"
#			with open(save , "w") as file1:
#			for i in range(0, numpcomp): #for i in the range from 0 to the number of players
#					file1.write(str(hplay[i].name)) #write the appropriate player's name as a string
#					file1.write("\t") #tab
#					for j in hplay[i].hand: #for j in each players card list
#						myfile.write(str(j.val) #write the appropriate value of the card as a string
#						myfile.write(", ") # comma space
#					myfile.write("\n") #enter after the whole list is saved
#				print "Your game has been saved." #print
#				quit() #exit the program
#		#if they don't want to save and exit go back to the menu
#		elif sgame == "no":
#			Menu()
#	except ValueError: #if the user did not input 'yes' or 'no' give them another chance.
#		print "That is not proper input. Please type 'yes' or 'no'"

def HighScore_write(numcomp):


	if int(str(numcomp[0])) == 1:
		highscores = open("oneplayer.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		for i in q:
			print i
		highscores.close()
		highscores2 = open ("oneplayer.txt", "w")
		highscores2.write(str(q[-1]))
	elif int(str(numcomp[0])) == 2:
		highscores = open("twoplayers.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		for i in q:
			print i
		highscores.close()
		highscores2 = open ("twoplayers.txt", "w")
		highscores2.write(str(q[-1]))
	elif int(str(numcomp[0])) == 3:
		highscores = open("threeplayers.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		for i in q:
			print i
		highscores.close()
		highscores2 = open ("threeplayers.txt", "w")
		highscores2.write(str(q[-1]))

def HighScore_read(val):

	if int(val) == 2:
		highscores = open("twoplayers.txt", "r")
		b = highscores.readline()
		print "The highest score for two computer player go fish game is %s." % b

	elif int(val) == 3:
		highscores = open("threeplayers.txt", "r")
		b = highscores.readline()
		print "The highest score for three computer player go fish game is %s." % b

	elif int(val) == 4:
		highscores = open("fourplayers.txt", "r")
		b = highscores.readlines()
		print "The highest score for one computer player go fish game is %s." % b

def Start():
	while (True):
		print "What would you like to do?"
		print '''
			1. Play
			2. View high scores
			3. Rules
			4. Quit
		'''

		choice = raw_input("Choose a number. > " )

		try:
			choice = int(choice)

			if choice == 1:
				print "Good Luck!"
				Play()
			if choice == 2:
				print "High Scores"
				print "Based on number of computer players which high score would you like to see? (2-4)"
				players = raw_input(" > ")
				HighScore_read(players)

			if choice == 3:
				print """
The player to dealer's left starts. A turn consists of asking a specific player
for a specific rank. For example, if it is my turn I might say: 'Mary, please
give me your jacks'. The player who asks must already hold at least one card of
the requested rank, so I must hold at least one jack to say this. If the player
who was asked (Mary) has cards of the named rank (jacks in this case), she must
give all her cards of this rank to the player who asked for them. That player
then gets another turn and may again ask any player for any rank already held by
the asker.

If the person asked does not have any cards of the named rank, they say 'Go
fish!'. The asker must then draw the top card of the undealt stock. If the
drawn card is the rank asked for, the asker shows it and gets another turn.
If the drawn card is not the rank asked for, the asker keeps it, but the turn
now passes to the player who said 'Go fish!'.

As soon as a player collects a book of 4 cards of the same rank, this must
be shown and discarded face down. The game continues until either someone
has no cards left in their hand or the stock runs out. The winner is the player
who then has the most books.
				"""
			if choice == 4:
				exit()
		except ValueError:
			print "I don't know what that means."

Start()
