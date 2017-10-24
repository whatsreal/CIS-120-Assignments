import random
class Dice(object):
	def __init__(self):
		self.my_val = 0
		
	def myroll(self):
		x = random.randint(1, 6)
		self.my_val = x