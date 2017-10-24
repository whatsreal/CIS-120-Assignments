#Brian Jansen
#Ex 31
#Study drills were done in the form of beefing up this script and then adding a third door.  

import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
print "You enter a dark room with three doors."
print "Do you go through door #1, #2, or door #3?"

door = raw_input("> ")

if door == "1":
	os.system('cls' if os.name == 'nt' else 'clear')
	print "There's a giant bear here eating a confetti cake.  What do you do?"
	print "1. Take the cake!"
	print "2. Scream at the bear!"
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear
		
elif door == "2":
	os.system('cls' if os.name == 'nt' else 'clear')
	print "You stare into the endless abyss of Cthulhu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insinity rots your eyes into a pool of muck.  Good job!"
		
elif door == "3":
	os.system('cls' if os.name == 'nt' else 'clear')
	print "There are 5 pizzas.  One is poisoned, which pizza do you eat?"
	pizza = input("(1-5) ")
	poisoned = random.randint(1,5)
	if pizza <= 5 and pizza >= 1:
		if pizza != poisoned:
			os.system('cls' if os.name == 'nt' else 'clear')
			print "Cool you survived.  For now.  Pizza #%r was the poisoned pizza." % poisoned
			print "Now you see 3 levers.  One sets you free, the others give you a colonoscopy."
			print "Which lever do you choose?"
			lever = input("(1-3) ")
			freedom = random.randint(1,3)
			if lever <= 3 and lever >= 1:
				if lever == freedom:
					print "Congratulations, you've escaped wherever you were.  Some sort of temple or something."
				else:
					print "Oops, wrong lever the correct one was #%r.  You get the colonoscopy." % freedom
			else:
				print "That's not one of your options.  You die of starvation."
		else:
			print "You dead, foo!"
	else:
		print "That's not one of the options.  You die of starvation."
else:
	print "I guess you figured out you don't have to go through a door.  You fail anyways.  (Just out of spite)"
					
