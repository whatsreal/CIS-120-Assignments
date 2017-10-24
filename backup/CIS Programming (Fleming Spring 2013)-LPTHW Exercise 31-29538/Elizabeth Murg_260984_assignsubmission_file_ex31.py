#Elizabeth Murg	
#Assignment Number 10. 2/10/2014

#door 3 is my addition for study drill
#introduction to the game. will print
print "You enter a dark room with two doors. Do you go through door #1, door #2 or door #3?"

#giving the user the option to input a choice to the above question.
door = raw_input ("> ")

#this will give options based on what door the user chooses. if door 1 it will branch into 2 more choices 
if door == "1":
	print "There's a giant bear here eating a cheese cake."
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear= raw_input ("> ")
#this shows what will happen based off the choices after door 1
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
#basically the same thing as 1. so no point in recommenting. 
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input ("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
elif door == "3":
	print "You have reached heaven now."
	print "1. Bliss"
	print "2. Torture"
	
	easychoice = raw_input ("> ")
	
	if easychoice == "1":
		print "You have made it to eternal joy. Congratulations!"
	else: 
		print "You are pretty dumb for choosing torture, and probably deserve to be here in eternal torment. Good luck."
else:
	print "You stumble around and fall on a knife and die."
	
