#Marta Sobey 
#Assignment Number 40. 2/17/14

#assigns a class with name Song
class Song(object):
	#defines the class
	def __init__(self, lyrics):
		self.lyrics = lyrics
		#defines the class
	def sarcastic(self):
		print "That wasn't very catchy"
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
#assigns a variable to the song lyrics	
happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
#assigns a variable tot he song lyrics
bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])
#calls the variable to do what is defined in the sing_me_a_song definition
happy_bday.sing_me_a_song()
#calls the variable to do what is defined in the sing_me_a_song definition
bulls_on_parade.sing_me_a_song()
#My version
class Songs(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
words = ["Mary had a little lamb", "Little lamb", "Little lamb"]			
Mary_Had_A_Little_Lamb = Song(words)

Mary_Had_A_Little_Lamb_Continued = Song(["Mary had a little lamb", "Its fur was white as snow"])

Mary_Had_A_Little_Lamb.sing_me_a_song()
Mary_Had_A_Little_Lamb.sarcastic()

Mary_Had_A_Little_Lamb_Continued.sing_me_a_song()

#I tried to read about OOP but it makes no sense to me