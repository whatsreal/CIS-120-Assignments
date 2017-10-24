#Marta Sobey 
#Assignment Number 36. 2/17/14


from sys import exit
#defines
def Marta_room():
	print "This room is super messy. How long are you going to spend cleaning?"
	#prompts the user to interact with the program
	next = raw_input("> ")
	how_long = int(next)
	if how_long < 10:
		
		dead("That is not enough time to get everything clean.")
		
	elif how_long < 50:
		print "Nice, you're all done. The room is now clean. You win!"
		exit(0)
	else:
		dead("You take too long cleaning!")
#defines		
def Cari_room():
	print "Cari is in here."
	print "She is talking on the phone with a friend."
	print "The door is blocked with all her clothes and nobody can leave."
	print "How are you going to move the clothes and leave her room?"
	Cari_moved = False
	
	while True:
		#prompts the user to interact with the program and assigns their input to the variable next
		next = raw_input("> ")
		#goes through a series of if, elif, else statements telling shell what to print based on which statement is true.
		if next == "take phone":
			dead("She looks at you then slaps you until you give her her phone back.")
		elif next == "tease her" and not Cari_moved:
			print "Cari has moved her clothes from the door. You can go through it now."
			Cari_moved = True
		elif next == "tease her" and Cari_moved:
			dead("Cari gets mad and kicks you out of her room.")
		elif next == "open door" and Cari_moved:
			Marta_room()
		else:
			print "I got no idea what that means."
#defines			
def Michelle_room():
	print "As you walk in you see Michelle."
	print "She looks annoyed at you because she is working."
	print "Do you close the door and leave?"
	#prompts the user to interact with the program and assigns their input to the variable next
	next = raw_input("> ")
	#goes through a series of if, elif, else statements telling shell what to print based on which statement is true.
	if "yes" in next:
		start()
	elif "no" in next:
		dead("Well that was dumb. She got you kicked out!")
	else:
		Michelle_room()
#defines		
def dead(why):
	print why, "Game over!"
	exit(0)
#defines	
def start():
	print "You are in the hallway."
	print "There is a door to your right and left."
	print "Which one do you take?"
	#prompts the user to interact with the program and assigns their input to the variable next
	next = raw_input("> ")
	#goes through a series of if, elif, else statements telling shell what to print based on which statement is true.
	if next == "left":
		Cari_room()
	elif next == "right":
		Michelle_room()
	else:
		dead("You stay in the hallway and get killed.")
		
start()

#to expand it I could add other rooms in front and behind. 