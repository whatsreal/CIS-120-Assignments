#Marta Sobey
#Final
#War

filename = "highscores.txt" #I send the high scores to this file
filename2 = "savedgame.txt" #I save the players' names and lists herefilename = "highscores.txt" #I send the high scores to this file
import random #used for the shuffle
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
			suitcounter = suitcounter + 1 #increase the suitcounter by each suit
AddCardsToDeck() #call this function
def Help():
	#just prints out instructions to help the user.
	print "If you want to start a new game press the key labelled '1'."
	print "If you want to just leave this game completely without saving it press the key labelled '2'."
	print "If you want to leave this game and save it press the key labelled '3'."
	print "If you need help press the key labelled '4'."
	print "If you just want to continue on with your game press the key labelled '5'."
	Menu() #goes back to the menu

def Quit():
	try: #make sure the input is readable. 
		leave = raw_input("Are you sure you want to quit this game? (yes or no) > ") #make sure the user really wants to quit the game
		#if they do want to leave say Goodbye and exit the program
		if leave == "yes":
			print "Goodbye"
			quit()
		#if they don't want to leave go back to the menu	
		elif leave == "no":
			Menu()
	except ValueError: #if the user inputs anything but "yes" or "no", start over and have them try again.
		print "That is not proper input. Please type 'yes' or 'no'"	
def Save():
	"""this is going to save the game where the user leaves off.
		It will save the names of the players and their lists."""
	try: #make sure the user input is readable
		#ask if the user really wants to save the game and exit
		byebye = raw_input("Are you sure you want to save this game and exit? (yes or no) > ")
		print #prints an empty line
		if byebye == "yes":
			with open(filename2, "w") as myfile: #open the file assigned that file name to write to
				for i in range(0, numplayers): #for i in the range from 0 to the number of players
					myfile.write(str(playerlist[i].name)) #write the appropriate player's name as a string
					myfile.write("\t") #tab
					for j in playerlist[i].cardlist: #for j in each players card list
						myfile.write(str(j.value)) #write the appropriate value of the card as a string
						myfile.write(" ") #space
						myfile.write(str(j.suit)) #write the appropriate suit of the card as a string
						myfile.write(" ") #space
						myfile.write(str(j.displayValue)) #write the appropriate display value of the card as a string
						myfile.write(", ") # comma space
					myfile.write("\n") #enter after the whole list is saved
				print "Your game has been saved." #print
				quit() #exit the program
		#if they don't want to save and exit go back to the menu
		elif byebye == "no":
			Menu()
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
					saved_name = word[0].split("\t")[0] #the name is the first thing in the first assigned 'word'
					playerlist.append(Player(saved_name)) #add that saved name to the list playerlist as an object of the class Player
					word[0] = word[0][len(saved_name) + 1:] #the first 'word' 
					for i in word: #for each thing in 'word'
						component = i.split(" ") #assign component to each item in what was already separated. These are separated by one space.
						if len(component) == 3: #if the length of this variable is three (value, suit, and display value).
							saved_value = component[0] #the value is the first thing
							saved_suit = component[1] #the suit is the second thing
							saved_displayvalue = component[2] #the display value is the third value
							saved_list = Cards(saved_suit, int(saved_value), saved_displayvalue) #assign a variable to the Card object we just made
							playerlist[len(playerlist)-1].cardlist.append(saved_list) #add the card we just made to the appropriate player's card list
				else:
					print "You do not have any games saved"
					Menu()
		numplayers = len(playerlist) #define a variable

		Play() #call the function Play	
	#if they didn't actually want to play the saved game go back to the menu.
	elif areyousure == "no":
		Menu()
	# if they typed anything else just go back to the Menu	
	else:
		Menu()
		
def Instructions():
	"""prints out instructions on how to play game"""
	print "The object of the game is to get all the cards in the deck in the least number of turns."
	print "Aces have a value of 14, the 2's have a value 2, the 3's have a value of 3, and so forth to 10. The jacks then have values of 11, the queens have values of 12, and the kings have values of 13."
	print "To start the game each player will receive the same number of cards from a 52 card deck"
	print "Each round every player will show the first card in their deck. The player who plays a card that has the largest value receives all the cards that were played."
	print "If their is a tie for the highest card (for instance if one player plays a 2, another player plays a 5, and another player plays a 5), the second card in each players deck is played."
	print "If multiple wars happen in a row the same process occurs and the player who finally has the highest card without being tied receives all the cards from all the different rounds of wars."
	print "If their is an instance where two people tie but another card is played by a third player which is larger, the third person receives all of the cards and no war occurs."
	print "For a three or four person game, even if everybody doesn't tie for the highest value, everybody still plays a second card with the possibility of winning."
	print "Once a player runs out of cards, they loose, but if two or more players remain with cards, the game will continue."
	print "High scores are based on how many rounds it takes to win"
	Menu() #go back to the menu
def Menu():
	"""give the players options as to what they want to do"""
	while(True):
		try: #make sure the input is readable
			#print "\n" * 52 #clear the screen
			#ask the users what they want to do
			print "\n" *50
			choice = raw_input(" Press 1 to play a new game \n \n Press 2 to resume a saved game \n \n Press 3 to quit \n \n Press 4 to save \n \n Press 5 for help \n \n Press 6 for instructions on how to play \n \n Press 7 to view high scores \n \n Press 8 to continue with your game \n \n > ")
			#convert that input to an integer
			print "\n" *5
			choice = int(choice)
			print #print an empty line
			if choice == 1:
				NewGame() #call NewGame function
			elif choice == 2:
				with open(filename2, "r") as f: #opens the file to read
					for str in f: #for each string in the file
						print "for loop"
						PlaySavedGame()
				print "You do not have any games saved"	
				print "\n" *5
				pause = raw_input("Hit enter to return to the main menu > ")
			elif choice == 3:
				Quit() #call Quit function
			elif choice == 4:
				Save() #call Save function
			elif choice == 5:
				Help() #call Help function
			elif choice == 6:
				Instructions() #call Instructions function
			elif choice == 7:
				Highscores() #call Highscores function
			elif choice == 8:
				Play() #call Play function
		except ValueError: #if the input isn't readable give them another chance
			print "That is not proper input. Please type a number. (1, 2, 3, 4, 5, 6, 7, or 8)"	
				
def NewGame():
	print "\n" * 52 #clear the screen
	
	print "Welcome to the game of War!"
	print
	random.shuffle(deck) #shuffle the deck
	#assign variables
	global numcards
	global playerlist
	global numplayers
	global winnercards
	playerlist = []
	numplayers = 0
	AddCardsToDeck()
	try: #make sure the input is readable
		numplayers = raw_input("Number of players? ") #get the number of players
		numplayers = int(numplayers) #convert that to an integer
		print #print a blank line
			
		for i in range(0, numplayers): #for i from 0 to the number of players
			playername = raw_input("Name of player > ") #get the names of the players
			print #print a blank line
			playerlist.append(Player(playername)) #make that input into an object from the Player class and add those the the playerlist list
		numcards = 52//numplayers #assign the variable numcards to the appropriate number of cards based on the number of players
		
		
		for i in range(0, numcards): #for i from 0 to the number of cards
			for j in range(0, len(playerlist)): #for j from 0 to the number of players
				playerlist[j].add(deck[i]) #add cards to the players' lists one at a time
				del deck[i] #after adding a card from the deck to a player's list, delete that card from deck list
		winnercards = [] #assign a variable		

	except ValueError: #if the input is not readable give the user another chance
		print "That is not proper input. When asked for number of players please type a valid number(2, 3, or 4)."

	Play() #call the function Play again

def Highscores():
	"""read the high scores"""
	with open(filename, "r") as f: #open the appropriate file to read
		print "Number of players", "Scores", "Player Names"
		for line in f: #for each line in the file
			word = line.split() #split each line
			if len(word) > 0:
				numplayers = word[0] #the first word is the number of players
				score = word[1] #the second word is the score
				name = word[2] #the third word is the name
				print "\t", numplayers, "\t", score, "\t", " "*5, name #if the score is four digits or greater it does not display nicely. You said that was ok.

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
		#raw_input("Anybody press enter to continue on to the next set of cards played")
		print "\n" * 35 #clears the screen
		for i in range(0, numplayers): #for i from 0 to the number of players
			if len(playerlist[i].cardlist) > 0 and len(playerlist) > 1: #checking to make sure all players have enough cards in their list to play
				print playerlist[i].name, "has enough cards to continue" #name of player then print statement
				print #print blank line
			else: #if one player doesn't have enough cards to continue
				print playerlist[i].name, "does not have enough cards to continue. You are out." #player name then print statement
				pause = raw_input() #pause the game
				print #print a blank line
				del playerlist[i] #delete that player from playerlist
				numplayers = numplayers - 1 #change the number of players
				print "It is now a", numplayers, "player game." #print statement then number of players then print statement
				break #break out
		if len(playerlist) == 1: #if their is only 1 player left in the game
				print playerlist[0].name, " is the winner!" #name of player then print statement
				print #print blank line
				winnername = playerlist[0].name #assign winner to the player's name
				print "Your score was, ", highscore #print statement then the high score
				
				next_highscore = HighScoreList(numplayers,highscore,playerlist[0].name) #assign next_highscore to the object of the class HighScoreList with the information we just retrieved
				next_highscore.readhighscore() #take the information we just got and take it to def readhighscore
				next_highscore.addhighscore(numplayers, highscore, playerlist[0].name) #take the information we just got and take it to def addhighscore passing in those variables
				#next_highscore.writehighscore() #take the information we just got and take it to def writehighscore
				winner = True #change the variable name to get out of the while loop
				Menu()
		comparecards = [] #assign a variable to an empty list
		print "\n" *12 #clear the screen

		for i in range(0, numplayers): #for i from 0 to number of players
			print "It is", playerlist[i].name, "'s turn"
			again = raw_input("press enter to play your next card")
			print playerlist[i].name, "'s card:", playerlist[i].cardlist[0].displayValue, #print player name then print statement then the display value of the first card in their list
			print "of", playerlist[i].cardlist[0].suit #print statement continued on the last line then the suit of the player's first card
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
					print "There is a war!" 
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
		print playerlist[winnerIndex].name, "wins all those cards" #print the winner's name then a print statement
		print "\n" * 20 #clear the screen


		try: #make sure the input is readable
			#continue or not question
			menuorexit = raw_input("Press 1 to continue playing or 2 to go to the menu > ")
			if menuorexit == "1":
				Play() #call Play function
			elif menuorexit == "2":
				Menu() #call Menu function
			
		except ValueError: #if anything else give the user another try to get the input right
			print "That is not proper input. Please type a number (1 or 2)."
		print "\n" * 40	 #clear the screen
	exit()	#exit the program
Menu()	#start by calling the menu
#playagain = raw_input("Press enter key to continue")