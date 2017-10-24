# Card Game
#
# In this game, you have to find matching pairs of cards.

from sandbox import *
from random import shuffle
from sys import exit 

nums = []
AI_memory = []
AI_Score = 0
Player_Score = 0

def flip():
	"""Allows the user to flip over two cards. Checks for a match and for errors"""
	flips = 0
	fliped_cards = []
	global nums
	nums = []
	while flips < 2:
		flips += 1
		print "Which card would you like to flip? (enter a number) > "
		number = raw_input()
		try:
			number = int(number)
			nums.append(number)
			if number > rows*columns:
				return "E1"
			elif a_entry.already_flipped(int(number)) == True:
				nums.append(number)
				return "E3"
			else:
				board, card = a_entry.flip_card(number)
				print 50*'\n' + board 
				fliped_cards.append(card)
		except ValueError:
			print "Enter a number"
			fliped_cards.append("P")
	try: 
		int(fliped_cards[0])
		int(fliped_cards[1])
		if fliped_cards[0] == fliped_cards[1]:
			return "Y"
		else:
			return "N"
	except ValueError:
		if len(nums) == 1:
			print "Enter a number"
			a_entry.unflip_card(int(nums[0]))
		else:
			print "Enter a number"

def AI_flip():
	"Allows the computer player to flip over two cards."
	global AI_memory           
	global AI_Score
	temp_mem = []
	AI_nums = []
	shuffle(AI_memory)
	print "Computer's turn"
	board, card1 = a_entry.flip_card(AI_memory[0])
	board, card2 = a_entry.flip_card(AI_memory[1])
	print board
	AI_nums.append(card1)
	AI_nums.append(card2)
	if AI_nums[0] == AI_nums[1]:
		print "Computers cards match."
		AI_Score += 1 
		AI_memory.remove(AI_memory[0])
		return "Y"
	else:
		a_entry.unflip_card(AI_memory[0])
		a_entry.unflip_card(AI_memory[1])
		print "Computers cards don't match."
		return "N"
	

while True:
	user_reply = raw_input("""    MEMORY by Justin Small. 
	
	What would you like to do? 
	1. Play a Game
	2. Search a High Score
	3. Read the Rules
	4. Load a Game 
	5. Quit
	> """) 
	
	while user_reply == '1':
		print "You must enter at least one even number", '\n', 40*'-'
		rows = raw_input("How many rows would you like your board to have? > ")
		print 40*'-'
		columns = raw_input("How many columns would you like your board to have? > ")	
		AIP = raw_input(50*'\n' + "Play against the computer? (y/n) >")
		if AIP == "n":
			try:
				rows = int(rows)
				columns = int(columns)
				a_entry = memory_game(rows,columns)
				answer = a_entry.create_board()
				screen = a_entry.blank_board()
				print 50*'\n' + screen
				score = 0
				while screen.find("S") and screen.find("E") == -1:
					answer = flip()
					if answer == "Y":
						tempboard = open('blank','r')
						status = tempboard.read()
						if status.count("X") < 1:
							print "YOU WIN!"
							print "Score:", score + 1
							name = raw_input("Enter your name > ")
							a_entry.high_scores(name, score+1)
							exit(0)
						else:
							print "Good job, cards match!"
							print "Save game and exit? (y/enter)"
							save = raw_input()
							if save == "y":
								name = raw_input("What do you want to call the game? > ")
								a_entry.save_game(name)
								exit(0)
					
					elif answer == "N":
						print "Sorry, no match. Try again."
						tempboard = open('blank','r')
						status = tempboard.read()
						a_entry.unflip_card(int(nums[0]))
						print a_entry.unflip_card(int(nums[1]))
						print "Save game and exit? (y/enter)"
						save = raw_input()
						if save == "y":
							name = raw_input("What do you want to call the game? > ")
							a_entry.save_game(name)
							exit(0)
					
					elif answer == "E1":
						if len(nums) == 2:
							print "E1"
							print "ERROR: The board does not have that many cards."
							a_entry.unflip_card(int(nums[0]))
						else:
							print "E2"
							print "ERROR: The board does not have that many cards."
			
					elif answer == "E3":
						if len(nums) == 3:
							print "E3"
							print "ERROR: That card has already been flipped."
							a_entry.unflip_card(int(nums[0]))
						else:
							print "E4"
							print "ERROR: that card has already been flipped."
					
					else:
						a_entry.blank_board()
						user_reply = ''
					
					score += 1
			
			except ValueError:
				print "Please enter a number"
			
		
		if AIP == "y":
			try:
				rows = int(rows)
				columns = int(columns)
				a_entry = memory_game(rows,columns)
				answer = a_entry.create_board()
				screen = a_entry.blank_board()
				print 50*'\n' + screen
				for i in range(rows*columns):
					AI_memory.append(i+1)
				while screen.find("S") and screen.find("E") == -1:
					answer = flip()
					if answer == "Y":
						tempboard = open('blank','r')
						status = tempboard.read()
						if status.count("X") < 1:
							print "Score: ", Player_Score
							print "Computer Score: ", AI_Score
							if Player_Score > AI_Score:
								print "YOU WIN!"
							else:
								print "You Lose."
							exit(0)
						else:
							print "Good job, cards match!"
							print "Save game and exit? (y/enter)"
							save = raw_input()
							if save == "y":
								name = raw_input("What do you want to call the game? > ")
								a_entry.save_game(name)
								exit(0)
							AI_memory.remove(int(nums[0]))
							AI_memory.remove(int(nums[1]))
							AI_answer = AI_flip()
							if AI_answer == "Y":
								tempboard = open('blank','r')
								status = tempboard.read()
								if status.count("X") < 1:
									print "Score =", Player_Score
									print "Computer Score: ", AI_Score
									if Player_Score > AI_Score:
										print "YOU WIN!"
									else:
										print "You Lose."
									exit(0)
								else:
									print "" 
							Player_Score += 1
					
					elif answer == "N":
						print "Sorry, no match."
						tempboard = open('blank','r')
						status = tempboard.read()
						a_entry.unflip_card(int(nums[0]))
						print a_entry.unflip_card(int(nums[1]))
						print "Save game and exit? (y/enter)"
						save = raw_input()
						if save == "y":
							name = raw_input("What do you want to call the game? > ")
							a_entry.save_game(name)
							exit(0)
						AI_flip()
						
					elif answer == "E1":
						if len(nums) == 2:
							print "E1"
							print "ERROR: The board does not have that many cards."
							a_entry.unflip_card(int(nums[0]))
						else:
							print "E2"
							print "ERROR: The board does not have that many cards."
			
					elif answer == "E3":
						if len(nums) == 3:
							print "E3"
							print "ERROR: That card has already been flipped."
							a_entry.unflip_card(int(nums[0]))
						else:
							print "E4"
							print "ERROR: that card has already been flipped."
					
					else:
						a_entry.blank_board()
						user_reply = ''
			
			except ValueError:
				print "Please enter a number"
				user_reply = ''
	
	
	while user_reply == '2':
		rows = raw_input("For what width? (# of rows) ")
		columns = raw_input(50*'\n'+"And for what hight (# of columns) "+2*"\n")
		try:
			rows = int(rows)
			columns = int(columns)
			a_entry = memory_game(rows, columns)
			print 50*"\n" + "HIGH SCORES" + "\n" + "-----------"
			a_entry.read_scores(rows, columns)
			print "\n"
			user_reply = ''
		except ValueError:
			print "Please enter a number"
		
	
	
	while user_reply == '3':
		ruledoc = open('rules', 'r')
		print 2*"\n" + ruledoc.read()
		user_reply = ''
		
	
	while user_reply == '4':
		rows = input("How many rows were in the game? > ")
		columns = input("How many columns were in the game > ")
		game = raw_input("What game would you like to load? > ") 
		a_entry = memory_game(rows, columns) 
		game = a_entry.load_game(game)
		while game.find("N") == -1:
			answer = flip()
			score = 0
			if answer == "Y":
				tempboard = open('blank','r')
				status = tempboard.read()
				if status.count("X") < 1:
					print "YOU WIN!"
					print "Score:", score + 1
					name = raw_input("Enter your name > ")
					a_entry.high_scores(name, score+1)
					exit(0)
				else:		
					print "Good job, cards match!"
					print "Save game and exit? (y/enter)"
					save = raw_input()
					if save == "y":
						name = raw_input("What do you want to call the game? > ")
						a_entry.save_game(name)
						exit(0)
					
			elif answer == "N":
				print "Sorry, no match. Try again."
				tempboard = open('blank','r')
				status = tempboard.read()
				a_entry.unflip_card(int(nums[0]))
				print a_entry.unflip_card(int(nums[1]))
				print "Save game and exit? (y/enter)"
				save = raw_input()
				if save == "y":
					name = raw_input("What do you want to call the game? > ")
					a_entry.save_game(name)
					exit(0)
					
			elif answer == "E1":
				if len(nums) == 2:
					print "E1"
					print "ERROR: The board does not have that many cards."
					a_entry.unflip_card(int(nums[0]))
				else:
					print "E2"
					print "ERROR: The board does not have that many cards."
		
			elif answer == "E3":
				if len(nums) == 3:
					print "E3"
					print "ERROR: That card has already been flipped."
					a_entry.unflip_card(int(nums[0]))
				else:
					print "E4"
					print "ERROR: that card has already been flipped."
					
			else:
				a_entry.blank_board()
				user_reply = ''
					
			score += 1
		print game
		print 40*"-"
		user_reply = ''
	
	while user_reply == '5':
		exit(0)
