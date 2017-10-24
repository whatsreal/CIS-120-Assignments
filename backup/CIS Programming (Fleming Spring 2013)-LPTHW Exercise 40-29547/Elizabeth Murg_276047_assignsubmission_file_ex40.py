#Elizabeth Murg
#Assignment Number 40. 2/17/2014.

#Study Drill 1. 

#here I define a variable with lyrics to a song
my_song_as_a_variable = "Just doing what I'm told. \n\t\tIt seems very bold. \nBut I have no choice.\n\t\tMaybe I'll lose my voice."

#then i make a new class
class Song(object):
#here i def new functions 
	def __init__(self, lyrics):
		self.lyrics = lyrics
	#this function will tell make the program print out my variable and then 
#it will also print out the lines of my other songs	
	def sing_me_a_song(self):
		print my_song_as_a_variable
		for line in self.lyrics:
			print line
#here i write out the songs.
happy_bday = Song (["Happy birthday to you",
					"I don't want to get sued", 
				    "So I'll stop right there"])

bulls_on_parade = Song (["They rally around the family",
						 "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()



my_song = Song (["Just doing what I'm told. \n\t\tIt seems very bold. \nBut I have no choice. \n\t\tMaybe I'll lose my voice."])

my_song.sing_me_a_song()