#Brian Jansen
#Ex 40

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def singmeasong(self):
		for line in self.lyrics:
			print line
			
happybday = Song(["Happy Birthday to you", "I don't want to get sued", "So I'll stop right there"])
bullsonparade = Song(["They rally around the family", "with pockets full of shells"])

happybday.singmeasong()
bullsonparade.singmeasong()

#Study Drills.
#1. I understand
#2-4. No
