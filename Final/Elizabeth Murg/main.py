from sys import exit
import time
import random
from DiceClass import *
from PlayerClass import *




def add_players():
		global myplayers
		num_play = raw_input("How many players would you like (excluding yourself, 1-3)? > ")
		time.sleep(2)
	
		try:
			num_play = int(num_play)
			b = ["Justin", "Marta", "Dan", "Moses", "Mikey", "Samson", "Angus", "Philemon", "Bob", "Mary", "Laura", "Piglet", "Tigger", "Billy", "Larry", "Michelle", "Nemo"]
			#syntax to put all three nums in one line?
			if num_play == 1 or num_play == 2  or num_play == 3:
				for i in range(0, num_play):
					player_name = random.choice(b)
					b.remove(player_name)
					sco_re = 0
					new_player = Player(player_name, sco_re)
					print "\n\n\nYou will be playing against %s!!!!!!" % player_name
					myplayers.append(new_player)
					time.sleep(2) 
			
			else:	
				print "\n\nMust be number between 1-3.\n\n"
				time.sleep(1)
				add_players()
			
		except ValueError:
			print "That is not an option." 
	
def Help_Function():
	file = open('HELP.txt', 'r')
	print file.read()
	time.sleep(2)
	b = raw_input( "> ")
	try:
		b = int(b)
		if b == 1:
			file2 = open('HELP2.txt', 'r')
			print "\n\n"
			print file2.read()
			z = raw_input("Return to the main menu? > ")
			try:
				if z == "RETURN":
					return 
				elif z == "NO":
					print "Goodbye."
					exit()
				
					
						
			except ValueError:
				print "That is not an option. Type in exactly as written either RETURN or NO."
		elif b == 2: 
			file3 = open('HELP3.txt', "r")
			print file3.read()
			z2 = raw_input("Return to the game? > ")
			try:
				if z2 == "RETURN":
					return 
				elif z2 == "NO":
					print "Goodbye."
					exit()
				
					
			except ValueError:
				print "That is not an option. Type in exactly as written either RETURN or NO."
		
			
		else: 
			print "That is not an option."
			Help_Function()
	
	except ValueError:
		print "That is not option. Please choose a number."
	
def myplay(val):
	global human 
	mydice = []
	my_vals = []
	time.sleep(2)
	print "IT'S YOUR TURN %s!!" % human.name
	
	for i in range(0,val):
		mydice.append(Dice())
	
	lines = ["\nThe roll is", "\nYour first roll is ", "Your second roll is ", "Your third roll is ", "Your fourth roll is ", "Your fifth roll is ", "Your sixth roll is ", "Your seventh roll is ", "Your eighth roll is ", "Your ninth roll is ", "Your tenth roll is "]
	
	while True:
		roll_1 = raw_input("\nRoll? > ") 
		try:
			
			if roll_1 == "yes":
				b = 0 
				
				for i in mydice:
						
					b += 1 
					i.myroll()
					my_vals.append(i.my_val)
					time.sleep(1)
					print lines[b] 
					print i.my_val
					print "\n"
				 
				max = 0
				for number in my_vals:
					if number > max:
						max = number 
				human.score = max
				human.HeldScores.append(human.score)
				print "\nThe maximum score is....%s!!!!!!!!!!!!!!" % human.score
				print "\n\n\n"
				break 
			elif roll_1 == "no":
				print '''What would you like to do:
						1. Exit
						2. Save and Exit Game
						3. Help
						'''
						
				action = raw_input("Choose a number. > ")
		
				try:
					action = int(action)
					 
					if action == 1:
						exit()
					
					if action == 2:
						print "Saving Game."
						Save_Game(val)
						exit()
						
					elif action == 3:
						Help_Function()
						
				except ValueError:
					print "I do not understand what that means."
					print "Please choose a number between 1 - 3."
					
		except ValueError:
			print "That is not an option. Please say either yes or no."
	
def compplay (val):
	myvals = []
	myDice = []
	
	
	for i in range(0,val):
		myDice.append(Dice())
		
	lines = ["The roll is", "The first roll is ", "The second roll is ", "The third roll is ", "The fourth roll is ", "The fifth roll is ", "The sixth roll is ", "The seventh roll is ", "The eighth roll is ", "The ninth roll is ", "The tenth roll is "]
	
	
	for j in range(len(myplayers)):
		time.sleep(3)
		print "\nNow rolling is....%s \n" % myplayers[j].name
		time.sleep(1)
		
		b = 0 
		myvals = []
		for i in myDice:
				
			b += 1 
			i.myroll()
			myvals.append(i.my_val)
			time.sleep(1)
			print lines[b] 
			print i.my_val
			print "\n"
		 
		max = 0
		for number in myvals:
			if number > max:
				max = number 
				
		myplayers[j].score = max
		myplayers[j].HeldScores.append(myplayers[j].score)
		
		time.sleep(1)
		print "\nThe maximum score is....%s!!!!!!!!!!!!!!" % myplayers[j].score
		print "\n\n\n"	
	
def Rounds(rounds):
	rounds_list = ["ROUND 1", "ROUND 2", "ROUND 3", "ROUND 4", "ROUND 5", "ROUND 6"]
	for i in reversed(range(1, int(rounds)+1)):
		print "\n\n\n\n***********************************************************************************************************************"
		print "\t\t\t\t\t\t\t %s." % rounds_list[i-1]
		print "***********************************************************************************************************************"	
		myplay(i)
		compplay(i)	
	
def Save_Game(val):
	savefile = open("save.txt", "w")
	savefile.write(str(val))
	savefile.write("\n")
	savefile.write(human.name)
	savefile.write(" ")
	savefile.write(str(human.score))
	savefile.write("\n")
	for i in range(len(myplayers)):
		savefile.write(myplayers[i].name)
		savefile.write(" ")
		savefile.write(str(myplayers[i].score))
		savefile.write("\n")
		
def Load_Game():
	global human 
	global myplayers 
	savefile = open("save.txt", "r")
	x = savefile.readline()
	y = savefile.readline()
	saved_human = y.split(" ")
	saved_player = Player(saved_human[0], int(saved_human[1]))
	comp_plays = []
	for str in savefile:
		if len(str) > 1:
			word = str.split(" ")
			saved_comp = Player(word[0], int(word[1]))
			comp_plays.append(saved_comp)
			
	human = saved_player
	myplayers = comp_plays
	Rounds(x)
round = []			
def the_Game():
	global human 		
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHELLO!!!! :) "
	human_name = raw_input("What is your name? ") 
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome %s!" % human_name
	print "You are now playing Going to Boston, the best dice game known to mankind."
	human = Player(human_name, 0)

	add_players()
						
	while True:		
		x = raw_input("\nAre you ready? > " )

	 
		if x == "yes":
			print "\n\nFirst, how many rounds of the game would you like to play?"
			print "Choose a number from 1 to 5."
		
			while True:
				rounds = raw_input("\tChoose a number. > ")
				try:
					rounds = int(rounds)
					round.append(rounds)
			
					if rounds <= 5:
						Rounds(rounds)
						break
				
					else:	
						print "\nThat's too many rounds. Choose a number 1 to 5."
				except ValueError:
					print "Please choose a number."
			break
		elif x == "no":
			
			print '''What would you like to do:
						1. Exit
						2. Save and Exit Game
						3. Help
					'''
						
			action = raw_input("Choose a number. > ")
	
			try:
				action = int(action)
					 
				if action == 1:
					exit()
					
				elif action == 2:
					print "Saving Game."
					Save_Game()
					print exit()
						
				elif action == 3:
					Help_Function()
						
			except ValueError:
				print "I do not understand what that means."
				print "Please choose a number between 1 - 3."
		
		else:
			print "\nThat is not an option. Please choose either yes or no."
winnerscore = []
def Winner():

	#To find who is the winner:
	hs = human.HeldScores
	human.finalscore = sum(hs)

	print "Your final score is %s." % human.finalscore


	comp_play_high = []
	high = 0
	for j in range(len(myplayers)):
		x = sum(myplayers[j].HeldScores)
		
		myplayers[j].finalscore = x 
		print "%s's final score is %s." % (myplayers[j].name, myplayers[j].finalscore)
		if myplayers[j].finalscore > high:
			high = myplayers[j].finalscore
			comp_play_high = []
			comp_play_high.append(myplayers[j])
		elif myplayers[j].finalscore == high:
			comp_play_high.append(myplayers[j])

			
		
	if comp_play_high[0].finalscore > human.finalscore:
		if len(comp_play_high) > 1:
			print "It is a tie between the following players!"
			for q in range(len(comp_play_high)):
				print comp_play_high[q].name
			winnerscore.append(comp_play_high[0].finalscore)
			for i in myplayers:
				myplayers.remove(i)
				
		else:
			print "The winner is %s." % comp_play_high[0]
			winnerscore.append(comp_play_high[0].finalscore)
			for i in myplayers:
				myplayers.remove(i)
		
		print "Thanks for playing! Better luck next time!"
		
		
	elif comp_play_high[0].finalscore == human.finalscore:
		
		print "It's a tie between %s and the following player(s)!" % (human.name)
		for w in range(len(comp_play_high)):
			print comp_play_high[w].name
		winnerscore.append(comp_play_high[0].finalscore)
		for i in myplayers:
			myplayers.remove(i)
		
	else:
		winnerscore.append(human.finalscore)
		print "YOU WIN!!!!!!!!!!!!!!!!!!!"
		print "YAYYYYYYYYYYYYYYYYYYYYYYYYY!\n\n"""	
		time.sleep(1)
		for i in myplayers:
			myplayers.remove(i)
						
def HighScore_write(round):
	
	
	if int(round[0]) == 1:
		highscores = open("oneround.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		
		highscores.close()
		highscores2 = open ("oneround.txt", "w")		
		highscores2.write(str(q[-1]))
	elif int(round[0]) == 2:
		highscores = open("tworound.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		 
		highscores.close()
		highscores2 = open ("tworound.txt", "w")		
		highscores2.write(str(q[-1]))
	elif int(round[0]) == 3:
		highscores = open("threeround.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		
		highscores.close()
		highscores2 = open ("threeround.txt", "w")		
		highscores2.write(str(q[-1]))
	elif int(round[0]) == 4:
		highscores = open("fourround.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
		
		highscores.close()
		highscores2 = open ("fourround.txt", "w")		
		highscores2.write(str(q[-1]))
		
	else:
		highscores = open("fiveround.txt", "r")
		b = highscores.readline()
		q = b.split(" ")
		q.append(winnerscore[0])
		q = [int(i) for i in q]
		q.sort()
	
		highscores.close()
		highscores2 = open ("fiveround.txt", "w")		
		highscores2.write(str(q[-1]))
		
def HighScore_read(val):
	
	
	if int(val) == 1:
		highscores = open("oneround.txt", "r")
		b = highscores.readlines()
		print "The highest score for one dice game is %s." % b
		
	elif int(val) == 2:
		highscores = open("tworound.txt", "r")
		b = highscores.readline()
		print "The highest score for two dice game is %s." % b
		
	elif int(val) == 3:
		highscores = open("threeround.txt", "r")
		b = highscores.readline()
		print "The highest score for one dice game is %s." % b
	elif int(val) == 4:
		highscores = open("fourround.txt", "r")
		b = highscores.readline()
		print "The highest score for one dice game is %s." % b
		
		
	else:
		highscores = open("fiveround.txt", "r")
		b = highscores.readline()
		print "The highest score for one dice game is %s." % b
		
	
	
myplayers = []	





	
#MAIN MENU: 
def Start():
	while (True):
		print "\n\n\nWelcome!"
		print "You are now in the main menu of Going to Boston :)"
		print "What would you like to do? > "
		print '''
			1. Play
			2. View High Scores
			3. Rules and Regulations
			4. Help
			5. Exit
		'''
		
		action9 = raw_input("Choose a number. > ")
		
		try:
			action9 = int(action9)
			
			if action9 == 1:
				print "\n\n\n\nPlay new or saved game?"
				action1 = raw_input(" > ")
				
				try: 
					if action1 == "new":
						print "STARTING NEW GAME." 
						the_Game()
						Winner()
						HighScore_write(round)
						time.sleep(2)
						print "\n\nTo play another game click 1 to exit click 5."
						
					elif action1 == "saved":
						x = open("save.txt", "r")
						y = x.readline()
						try:
							y = int(y)
							print "SAVED GAME!"
							Load_Game()
							Winner()
							HighScore_write(round)
							time.sleep(2)
							overwrite = open("save.txt", "w")
							overwrite.close
							print "To play another game click 1 to exit click 5."
						except ValueError:
							print "No saved game! Sorry. Start a new one please.\n\n\n\n"
							time.sleep(1)
							
				
				except ValueError:
					print "Please type new or saved."
				
			if action9 == 2:
				print "View High Scores."
				print "High scores based on number of rounds. Which round type do you want? (1-5)"
				roundnum = raw_input (" > ") 
				HighScore_read(roundnum)
				while True:
					print "\n\nView another? Type YES or MAIN MENU or EXIT."
					x = raw_input("> ")
					
					if x == "MAIN MENU":
						Start() 
					elif x == "EXIT":
						print "Goodbye."
						exit()
					elif x == "YES":
						print "\nHigh scores based on number of rounds. Which round type do you want? (1-5)"
						roundnum = raw_input (" > ") 
						HighScore_read(roundnum)
					else:
						print "Not an option. Going to main menu."
						Start()
					
					
					
				
					
				
			
			if action9 == 3:				 
				file4 = open('TUTORIAL.txt', "r")
				print file4.read()
				while True: 
					z3 = raw_input("Return to the main menu? > ")
				
					if z3 == "MAIN MENU":
						Start() 
					elif z3 == "NO":
						print "Goodbye."
						exit()
					
					break
			
			if action9 == 4:
				Help_Function()
				
			if action9 == 5:
				print "Exit."
				exit()
				
				
		except ValueError:
			print "That is not an option. Try again."
			
Start()				