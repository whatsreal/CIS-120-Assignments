
from HighScore import *

filename = "highscores.txt" #I send the high scores to this file

class HighScoreList(object):
	"""This class will allow multiple high scores to be saved to the file defined above and read back into the game."""
	def __init__(self, numplayers, score, name):
		self.highscorelist = []
		
	def readhighscore(self):
		"""This is going to read the high scores that are already in the file"""
		with open(filename, "r") as f: #opens the file to read
			for str in f: #for each string in the file
				if len(str) > 1: #if there is anything in the file
					word = str.split("\t") #each word is split by tabs.
					new_numplayers = word[0] #number of players is the first word in the file
					new_score = word[1] #score is the second word in the file
					new_name = word[2] #name is the third word in the file
					new_highscore = HighScore(new_numplayers, new_score, new_name) #creates a new object high score from the class HighScore with the new information.
					self.highscorelist.append(new_highscore) #add the new high score we created to the empty list we defined above in the init function called highscorelist

	def addhighscore(self,number,highscore,name):
		"""This is going to add more high scores to the file"""
		#defining variables
		new_numplayers = number
		new_score = highscore
		new_name = name
		new_highscore = HighScore(new_numplayers, new_score, new_name) #creating a new high score object from the HighScore class
		self.highscorelist.append(new_highscore) #adding that new high score to the highscorelist list
		
	def writehighscore(self):
		"""This is going to write the high scores out"""
		file = open (filename, "w"); #open the file defined about to write to
		for i in self.highscorelist: #for each thing in the highscorelist
			file.write(str(i.numplayers)) #write the the number of players
			file.write("\t") #tab
			file.write(str(i.score)) #write the score
			file.write("\t") #tab
			file.write(str(i.name)) #write the name
			file.write("\n") #enter