#Card Class
class card(object):
	"""Card object that stores various information about specific cards within the deck."""
	def __init__(self, suit, name, numval, numid):
		"""This function just stores the information."""
		self.suit = suit
		self.name = name
		self.numval = numval
		self.numid = numid
		if suit is "s" or suit is "c":
			self.color = "b"
		else:
			self.color = "r"
