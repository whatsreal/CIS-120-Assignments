#Marta Sobey 
#Assignment Number 45. 2/24/14
#importing exit to be used when the player dies
from sys import exit
#creating a class
class scene(object):
	print "You are in the hallway. There is a door on your right and a door on your left. Which one do you enter?"
	#defining a room
	def CarisRoom(self):
		print "You see Cari doing a puzzle that you want to do."
		print "What do you do?"
		print "Do you ask to join her, join her without asking, or take the puzzle and run?"
		#prompting the user for input
		action = raw_input ("> ")
		#if, elif, else statement
		if action == "ask to join her":
			print "Good job. She says yes and you too finish the puzzle together. You win!"
			#exiting the game
			return exit()
		elif action == "join her without asking":
			print "Oh no. She pushed you out in the hallway and locked the door."
			print "Do you want to go to the right again or do you want to try the left this time?"
			self.startroom()
		elif action == "take the puzzle and run":
			print "Bad choice. She goes and tells on you. You die!"
			return exit()
		else: 
			print "Not allowed. Try again."
			#returns the user to a specific point in the game so they can try again
			self.CarisRoom()
	#same as with CarisRoom
	def MichellesRoom(self):
		print "You see Michelle making stuff on her sewing machine"
		print "You are bored and want some company"
		print "What do you do? Try to get her attention, see she is working and quietly leave, join her and learn how to sew too."
		action = raw_input ("> ")
		if action == "try to get her attention":
			print "She gets annoyed by you making so much noise and kicks you out in the hallway."
			print "Do you want to try going to the left again or try the right this time?"
			self.startroom()
		elif action == "see she is working and quietly leave":
			print "You remain in the hallway and die of boredom. You're now dead!"
			return exit()
		elif action == "join her and learn how to sew too":
			print "You make a beautiful blanket that you sleep with that night. You win!"
			return exit()
		else:
			print "Not allowed. Try again!"
			self.MichellesRoom()
	def startroom(self):
		direction = raw_input ("> ")
		if direction == "right":
			self.CarisRoom()
		elif direction == "left":
			self.MichellesRoom()
		else:
			print "That was not one of your choices. Try again."
			self.startroom()
	
#calls the different function to run the game	
mygame = scene()
mygame.startroom()