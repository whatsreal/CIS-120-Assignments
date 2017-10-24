#Mason Hunter CIS 120
#Assignment 40
class Song(object): #makes a class and puts functions inside that class

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
#makes a variable and puts it into the song class          
happy_bday = Song(["Happy Birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
#same thing again                   
bulls_on_parade = Song (["They rally around the family",
                         "With pockets full of shells"])
                         
happy_bday.sing_me_a_song() #runs these variables with the functions in song class
bulls_on_parade.sing_me_a_song()

#SD 1:
twinkle = Song(["Twinkle twinkle little star, how I wonder what you are."])
#SD 2
baabaa = "BAA BAA blackseep have you any wool"
baabaa = Song()
#SD 3
Song(baabaa).sing_me_a_song()
