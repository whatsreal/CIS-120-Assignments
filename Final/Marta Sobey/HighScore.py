


class HighScore(object):
	"""This class allows high scores to be saved with the number of players playing, the winning score, and the winning player's name"""
	def __init__ (self, numplayers, score, name):
		self.numplayers = numplayers
		self.score = score
		self.name = name