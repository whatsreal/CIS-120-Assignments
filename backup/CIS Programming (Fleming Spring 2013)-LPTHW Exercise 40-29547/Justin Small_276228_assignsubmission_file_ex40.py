# Justin Small, Exercise 40, 2/16/2014

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

dare_you_to_move = Song(["I dare you to move",
                         "I dare you to move",
                         "I dare you to lift yourself up off the floor"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

dare_you_to_move.sing_me_a_song()


# Study Drills:
#1. Okay
#2. I think I did this yay!
#3. Not sure what part of it I would try to hack.
#4. Wow, this was a lot! 
