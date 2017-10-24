#Marta Sobey
#Final
#War

filename = "highscores.txt" #I send the high scores to this file
filename2 = "savedgame.txt" #I save the players' names and lists here.
import random #used for the shuffle
import time #used to pause the game while they are playing
#different files that hold my classes
from Cards import *
from Player import *
from HighScore import *
from HighScoreList import *
#defining variables that will be used later on
deck = []
playerlist = []
winnercards = []
numplayers = 0
highscore = 0
winner = False

def AddCardsToDeck():
	"""This is going to make the deck"""
	#defining variables
	global deck
	deckCounter = 0
	suitcounter = 1
	while (deckCounter <= 52): #only do 52 cards

		for suit in range(1, 5): #for each different suit (4 of them).
			if(suit == 1): #the first suit is hearts
				suit = "Hearts"
			elif(suit == 2): #the second suit is diamonds
				suit = "Diamonds"
			elif(suit == 3): #the third suit is spades
				suit = "Spades"
			elif(suit == 4): #the fourth suit is clubs
				suit = "Clubs"
			for value in range (2,13): #for each suit, add 13 different cards to each suit
				#defining the face cards and the Ace
				if(value == 11):
					displayValue = "Jack"
				elif(value == 12):
					displayValue = "Queen"
				elif(value == 13):
					displayValue = "King"

				elif(value == 14):
					displayValue = "Ace"
				else:
					displayValue = value #for the number cards, their value and display value are the same
				deck.append(Cards(suit, value, displayValue)) #Make Card objects with a suit, value, and display value and add them to the empty list deck.
				deckCounter = deckCounter + 1 #increase the deck counter for each card
			suitcounter = suitcounter + 1 #increase the suitcounter by 1 for each suit
AddCardsToDeck() #call this function
def Help():
	#just prints out instructions to help the user.
	print "\n" * 30 #clears the screen
	print "If you want to start a new game go to the Menu and press the key labeled '1'. \n"
	print "If you want to resume a saved game go to the Menu and press the key labeled '2'. \n"
	print "If you want to exit this game go to the Menu and press the key labeled '3'. \n"
	print "If you need help go to the Menu and press the key labeled '4'. \n"
	print "If you want to read the instructions on how to play this game go to the Menu and press the key labeled '5'. \n"
	print "If you want to view all the previous scores go to the Menu and press the key labeled '6'. \n"
	print
	pause = raw_input("Press enter to return to the Menu > ")
	Menu() #goes back to the Menu
def Quit():
	print "\n" * 25 #clear some lines
	print "Goodbye"
	print "\n" * 22 #clear the screen some
	quit() #stop the program

def Save():
	"""this is going to save the game where the user leaves off.
		It will save the names of the players and their card lists."""
	try: #make sure the user input is readable
		#ask if the user really wants to save the game and exit
		byebye = raw_input("Are you sure you want to save this game and exit? (yes or no) > ")
		print #prints an empty line
		if byebye == "yes":
			with open(filename2, "w") as myfile: #open the file assigned that file name to write to
				for i in range(0, numplayers): #for i in the range from 0 to the number of players
					myfile.write(str(playerlist[i].name)) #write the appropriate player's name as a string
					myfile.write("\t") #tab
					for j in playerlist[i].cardlist: #for each card in each players card list
						myfile.write(str(j.value)) #write the appropriate value of the card as a string
						myfile.write(" ") #space
						myfile.write(str(j.suit)) #write the appropriate suit of the card as a string
						myfile.write(" ") #space
						myfile.write(str(j.displayValue)) #write the appropriate display value of the card as a string
						myfile.write(", ") # comma space
					myfile.write("\n") #enter after the whole list is saved
			print "Your game has been saved." #print
			time.sleep(1) #pause the game to let the players see what is happening
			print "\n" * 10 #clear some lines
			exit() #exit the program
		#if they don't want to save and exit, go back to the Menu
		elif byebye == "no":
			PlayMenu() #go back to the menu
	except ValueError: #if the user did not input 'yes' or 'no' give them another chance.
		print "That is not proper input. Please type 'yes' or 'no'"
def PlaySavedGame():
	"""This will read the saved game information back in to play with"""
	#define variables
	global  playerlist
	global numplayers
	#Make sure they really want to start a saved game
	areyousure = raw_input("Are you sure you want to resume a previously started game? (yes or no) > ")
	print #print an empty line
	#if they do want to continue a saved game
	if areyousure == "yes":
		with open(filename2, "r") as saved_file: #open the appropriate file to read
			for str in saved_file: #for each string in the file
				if len(str) > 1: #make sure there is something in the file
					word = str.split(", ") #know each thing we are looking at is split by a comma and space
					saved_name = word[0].split("\t")[0] #the name is the first item in the first 'word'
					playerlist.append(Player(saved_name)) #add that saved name to the list playerlist as an object of the class Player
					word[0] = word[0][len(saved_name) + 1:] #the first 'word' excluding the name
					for i in word: #for each thing in 'word'
						component = i.split(" ") #assign component to each item in what was already separated. These are separated by one space.
						if len(component) == 3: #if the length of this variable is three (value, suit, and display value).
							saved_value = component[0] #the value is the first thing
							saved_suit = component[1] #the suit is the second thing
							saved_displayvalue = component[2] #the display value is the third value
							saved_list = Cards(saved_suit, int(saved_value), saved_displayvalue) #assign a variable to the Cards object we just made
							playerlist[len(playerlist)-1].cardlist.append(saved_list) #add the card we just made to the appropriate player's card list
				else:
					print "You do not have any games saved"
					Menu() #return to the menu if no game has been saved yet
		numplayers = len(playerlist) #define a variable

		Play() #call the function Play
	#if they didn't actually want to play the saved game go back to the menu.
	elif areyousure == "no":
		Menu() #return to menu
	# if they typed anything else just go back to the Menu
	else:
		print "That is not valid input. When asked you need to type 'yes' or 'no'."
		time.sleep(1) #pause the game for a second to let the players see what is happening
		Menu() #return to menu

def Instructions():
	"""prints out instructions on how to play game"""
	print "\n" * 10
	print "The object of the game is to get all the cards in the deck in the least number of turns. \n"
	print "Aces have a value of 14, the 2's have a value 2, the 3's have a value of 3, and so forth to 10. \n "
	print "The jacks then have values of 11, the queens have values of 12, and the kings have values of 13. \n"
	print "To start the game each player will receive the same number of cards from a 52 card deck. \n "
	print "Each round every player will show the first card in their deck. \n "
	print "The player who plays a card that has the largest value receives all the cards that were played. \n "
	print "If their is a tie for the highest card (for instance if one player plays a 5 and another player plays a 5), \n "
	print "2 cards from each players' deck are put face down and the third card in each players deck is played. \n "
	print "If multiple wars happen in a row the same process occurs and the player who finally has the highest card \n "
	print "without being tied receives all the cards from all the different rounds of wars. \n "
	print "If their is an instance where two people tie but another card is played by a third player which is larger, \n "
	print "the third person receives all of the cards and no war occurs. \n "
	print "For a three or four person game, even if everybody doesn't tie for the highest value, \n "
	print "everybody still plays a second card with the possibility of winning. \n "
	print "Once a player runs out of cards, they lose, but if two or more players remain with cards, the game will continue. \n "
	print "High scores are based on how many rounds it takes to win. \n "
	print "\n" * 10 #clear some lines

	pause = raw_input("Hit any key to return to the main menu > ")
	Menu() #go back to the menu
def Menu():
	"""give the players options as to what they want to do"""
	while(True): #start a while loop
		try: #make sure the input is readable
			print "\n" *36 #clear the screen
			#ask the users what they want to do
			choice = raw_input(" Press 1 to play a new game \n \n Press 2 to resume a saved game \n \n Press 3 to quit \n \n Press 4 for help \n \n Press 5 for instructions on how to play \n \n Press 6 to view previous scores \n \n > ")
			print "\n" *5 #clear some lines
			#convert that input to an integer
			choice = int(choice)
			print #print an empty line
			if choice == 1: #if they choose '1'
				NewGame() #call NewGame function
			elif choice == 2: #if they choose '2'
				with open(filename2, "r") as f: #opens the appropriate file to read
					for str in f: #for each string in the file
						PlaySavedGame() #call this function using the information that was just read in
				print "You do not have any games saved"	#if there was not any game saved
				print "\n" *5 #clear some lines
				pause = raw_input("Hit enter to return to the main menu > ")
			elif choice == 3: #if they choose '3'
				Quit() #call Quit function
			elif choice == 4: #if they choose '4'
				Help() #call Help function
			elif choice == 5: #if they choose '5'
				Instructions() #call Instructions function
			elif choice == 6: #if they choose '6'
				Highscores() #call Highscores function
		except ValueError: #if the input isn't readable give them another chance
			print "That is not proper input. Please return to the menu and type a number between 1 and 6. (1, 2, 3, 4, 5, or 6)"
			print "\n" * 4 #clear some lines
			pause = raw_input("Hit any key to return to the main menu > ")

def PlayMenu():
	"""give the players options as to what they want to do"""
	print "\n" * 10
	while(True): #start a while loop
		try: #make sure the input is readable
			print "\n" *32 #clear the screen
			#ask the users what they want to do
			choice = raw_input(" Press 1 to continue playing \n \n Press 2 to quit \n \n Press 3 to save this game and exit \n \n > ")
			print "\n" *5 #clear some lines
			#convert that input to an integer
			choice = int(choice)
			print #print an empty line
			if choice == 1: #if they choose '1'
				Play() #call Play function
			elif choice == 2: #if they choose '2'
				Quit() #call Quit function
			elif choice == 3: #if they choose '3'
				print "\n" * 3
				Save() #call Save function



		except ValueError: #if the input isn't readable give them another chance
			print "That is not proper input. Please type a number. (1, 2, 3, 4, 5, 6, 7, or 8)"
			print "\n" * 4 #clear some lines
			pause = raw_input("Hit any key to return to the main menu > ")
def NewGame():
	"""This function is going to get the players' names and add cards to their hands"""
	print "\n" * 52 #clear the screen

	print "Welcome to the game of War!"
	print #print empty line
	random.shuffle(deck) #shuffle the deck
	#assign variables
	global numcards
	global playerlist
	global numplayers
	global winnercards
	playerlist = []
	numplayers = 0
	AddCardsToDeck()
	numplayers = raw_input("Number of players? (2, 3, or 4) > ") #get the number of players

	if numplayers == "2" or numplayers == "3" or numplayers == "4":
		print #print a blank line
		numplayers = int(numplayers) #convert that to an integer
		for i in range(0, numplayers): #for i from 0 to the number of players
			playername = raw_input("Name of player > ") #get the names of the players
			print #print a blank line
			playerlist.append(Player(playername)) #make that input into an object from the Player class and add those the the playerlist list
		numcards = 52//numplayers #assign the variable numcards to the appropriate number of cards based on the number of players


		for i in range(0, numcards): #for i from 0 to the number of cards
			for j in range(0, len(playerlist)): #for j from 0 to the number of players
				playerlist[j].add(deck[i]) #add cards to the players' lists one at a time
				del deck[i] #after adding a card from the deck to a player's list, delete that card from the deck list
		winnercards = [] #assign a variable

	else: #if the input is not readable give the user another chance
		print "\n" * 5 #clear some lines
		print "That is not proper input. When asked for number of players please type a valid number (2, 3, or 4)."
		print "\n" * 3 #clear some lines
		pause = raw_input("Hit any key to return to the main menu > ")

	Play() #call the function Play

def Highscores():
	"""read the high scores"""
	scores = False
	maxscores = [] #assign a variable
	print "\n" *20
	with open(filename, "r") as f: #open the appropriate file to read
		print "Scores", "-", "Player Names"
		for line in f: #for each line in the file
			word = line.split() #split each line
			if len(word) > 0: #if there actually are scores already saved
				scores = True
				score = word[1] #the second word is the score
				name = word[2] #the third word is the name
				print " ", score, "\t", " "*6, name #if the score is four digits or greater it does not display nicely. You said that was ok.
				maxscores.append(score) #add all the scores to a list
			else:
				print "There are not any scores saved yet."
		print #print a blank line
		if scores == True:
			print "The score to beat is ", min(maxscores) #print the lowest score (because that is the best for this game_ to show what the score to beat is
		else:
			print "There have not been any scores yet."
		print "\n" * 5 #clear some lines

		pause = raw_input("Hit any key to return to the main menu > ")


def Play():
	"""Play the actual game"""
	#define variables
	global winnerIndex
	global playerlist
	global numplayers
	global winner
	global highscore
	global readhighscore
	global winnercards
	#pause = raw_input()
	while (winner == False): #will tell when to exit the game because somebody won
		highscore = highscore + 1 #keeps track of the score throughout the game
		print "\n" * 35 #clears the screen
		for i in range(0, numplayers): #for i from 0 to the number of players
			if len(playerlist[i].cardlist) > 0 and len(playerlist) > 1: #checking to make sure all players have enough cards in their list to play and that there are enough players to keep playing
				print playerlist[i].name, "has enough cards to continue" #name of player then print statement
				print #print blank line
			else: #if one player doesn't have enough cards to continue
				print playerlist[i].name, "does not have enough cards to continue. You are out." #player name then print statement
				pause = raw_input("Hit enter to continue > ")	#pause the game to let the players see what is happening
				print #print a blank line
				del playerlist[i] #delete that player from playerlist
				numplayers = numplayers - 1 #change the number of players
				print "It is now a", numplayers, "player game." #print statement then number of players then print statement
				break #break out of the for loop
		if len(playerlist) == 1: #if there is only 1 player left in the game
				print playerlist[0].name, " is the winner!" #name of player then print statement
				print #print blank line
				winnername = playerlist[0].name #assign winner to the player's name
				print "Your score was, ", highscore #print statement then the score
				time.sleep(2.5) #pause the game to let the players see what is happening
				print "\n" * 10
				next_highscore = HighScoreList(numplayers,highscore,playerlist[0].name) #assign next_highscore to the object of the class HighScoreList with the information we just retrieved
				next_highscore.readhighscore() #take the information we just got and take it to def readhighscore
				next_highscore.addhighscore(numplayers, highscore, playerlist[0].name) #take the information we just got and take it to def addhighscore passing in those variables
				next_highscore.writehighscore() #take the information we just got and take it to def writehighscore
				winner = True #change the variable name to get out of the while loop
				exit() #exit the program
		comparecards = [] #assign a variable to an empty list
		print "\n" *12 #clear some lines

		for i in range(0, numplayers): #for i from 0 to number of players
			print "\n" * 2 #clear some lines
			print "It is", playerlist[i].name, "'s turn:" #print statement then name of player then print statement
			print #print a blank line
			again = raw_input("Press enter to play your next card > ")
			print #print a blank line
			time.sleep(1) #pause the game for 1 second so they players can see what is happening
			print playerlist[i].name, "'s card:", playerlist[i].cardlist[0].displayValue, #print player name then print statement then the display value of the first card in their list
			print "of", playerlist[i].cardlist[0].suit #print statement continued on the last line then the suit of the player's first card
			time.sleep(1) #pause the game for 1 second so they players can see what is happening
			print #print blank line

			comparecards.append(playerlist[i].cardlist.pop(0)) #take that card and add it to the blank list. Then take that card out of the player's list
		#assign variables
		max = 0
		winnerIndex = 0
		for i in range(len(comparecards)): #for i from 0 to how many cards are in the comparcards list
			if comparecards[i].value > max: #used to find the highest card in the lsit
				winnerIndex = i #find who the winner is based on who's card was the highest
				max = comparecards[i].value #assign max to the highest value in the list

		winnerIndex = int(winnerIndex) #make winnerIndex an integer

		for i in range(0, len(comparecards)): #for i from 0 to how many cards are in the comparecards list
			if i != winnerIndex: #if there is a war but not with one's self

				if comparecards[i].value == comparecards[winnerIndex].value: #if their is a war
					print "\n" * 5
					print "There is a war!"
					print "\n" * 5
					pause = raw_input("Press enter to play the next set of cards > ") #pause the game
					for i in range(0, len(comparecards)): #for i from 0 to how many cards are in the comparcards list
						winnercards.append(comparecards[i])  #add all the cards that were in comparecards to the winnercards list
					for j in range(0, numplayers): #for j from 0 to the number of players
						if len(playerlist[j].cardlist) >= 3: #if each player has at least 3 cards, they can continue on and play the war
							winnercards.append(playerlist[j].cardlist.pop(0)) #take off the next card in the list and add it to the winnercards list
							winnercards.append(playerlist[j].cardlist.pop(0)) #take off the next card in the list and add it to the winnercards list

					comparecards = [] #assign variable
					Play() #call the Play function


		for i in range (0, len(comparecards)): #for i from 0 to how many cards are in the comparecards list
			playerlist[winnerIndex].add(comparecards.pop()) #adding one card from comparecards to the winner's list then deleting it from comparecards
		for i in range (0, len(winnercards)): #for i from 0 to how many cards are in the winnercarads list
			playerlist[winnerIndex].cardlist.append(winnercards.pop()) #add all the cards from winnercards to the winning player and take them out of the winnercards list at the same time
		time.sleep(1) #pause the game for 1 second to let the players see what is happening
		print "\n" * 5 #clear some lines
		print playerlist[winnerIndex].name, "wins all those cards" #print the winner's name then a print statement
		time.sleep(1)  #pause the game for 1 second to let the players see what is happening
		print "\n" * 5 #clear some lines



		#continue or not question
		menuorexit = raw_input("Press enter to continue playing or 2 to go to the Menu > ")
		if menuorexit == "2": #if they hit '2'
			PlayMenu() #call PlayMenu function
		else: #if they hit anything else
			Play() #call Play function

		print "\n" * 40	 #clear the screen
	exit()	#exit the program
Menu()	#start by calling the menu
