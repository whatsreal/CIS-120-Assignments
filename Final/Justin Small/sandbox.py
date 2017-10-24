from random import shuffle
import os.path

class memory_game(object):
	
	def __init__ (self, rows, columns):
		self.rows = rows
		self.columns = columns
		
	def blank_board(self):
		"""Creates a blank board
		   Assumes parameters rows*columns%2 == 0 and positive integers
		   Returns a rows x columns matrix, with blank cards."""
		cards = []
		if isinstance(self.rows, str) or isinstance(self.columns, str):
			return 'Enter numbers'
		elif self.rows < 0 or self.columns < 0:
			return 'Enter positive numbers'
		elif self.rows*self. columns > 20:
			return 'Enter smaller numbers'
		for i in range(0,self.rows*self.columns):
			if (self.rows*self.columns)%2 == 0:
				cards.append("X")
			else:
				return "Sorry that combination won't work, enter an even number"
		chunks = [cards[x:x+self.columns] for x in xrange(0, len(cards), self.columns)]
		chunks = "\n".join(str(x) for x in chunks)	
		blank = open('blank', 'w')
		blank.write(chunks)
		return chunks

	def create_board(self):
		"""Draws and stores an initial board
		   Assumes parameters rows*columns%2 == 0 and positive integers
		   Returns a rows x columns matrix, with random integers."""
		cards = []
		for i in range(0,(self.rows*self.columns)/2):
			cards.append(i)
		cards = cards*2
		shuffle(cards)
		chunks = [cards[x:x+self.columns] for x in xrange(0, len(cards), self.columns)]
		chunks = "\n".join(str(x) for x in chunks)
		board = open('board','w')
		board.write(chunks)
		return chunks
		
	def flip_card(self, num):
		"""Allows the user to select two cards, if they match, they stay flipped"
		   Assumes row and column exist as rows and columns of matrix
		   Returns the matching value of row(x), column(x)."""
		board_handle = open('board', 'r') 
		board = board_handle.read()
		board = board.replace('[','')
		board = board.replace(']','')
		board = board.replace(',','')
		board = board.replace(' ','')
		board = board.replace('\n','')
		board = board.rstrip()
		card = board[num-1]
		blank_handle = open('blank', 'r')
		blank = blank_handle.read()
		blank = blank.replace('[','')
		blank = blank.replace(']','')
		blank = blank.replace(',','')
		blank = blank.replace("'",'')
		blank = blank.replace('\n',' ')
		blank = blank.split(' ')
		blank[num-1] = card
		chunks = [blank[x:x+self.columns] for x in xrange(0, len(blank), self.columns)]
		chunks = "\n".join(str(x) for x in chunks)
		blank = open('blank', 'w')
		blank.write(chunks)
		return chunks, card
		
	def already_flipped(self, num):
		"""Checks to see if a card has already been flipped
		   Assumes num is a positive number
		   Returns a True if card != "X", else False""" 
		blank_handle = open('blank', 'r')
		blank = blank_handle.read()
		blank = blank.replace('[','')
		blank = blank.replace(']','')
		blank = blank.replace(',','')
		blank = blank.replace("'",'')
		blank = blank.replace('\n',' ')
		blank = blank.split(' ')
		if blank[num-1] != "X":
			return True
		else:
			return False 
			
	def unflip_card(self, num):
		"""Unflips the cards if they don't match."
		   Assumes row and column exist as rows and columns of matrix
		   Returns the matching value of row(x), column(x)."""
		blank_handle = open('blank', 'r')
		blank = blank_handle.read()
		blank = blank.replace('[','')
		blank = blank.replace(']','')
		blank = blank.replace(',','')
		blank = blank.replace("'",'')
		blank = blank.replace('\n',' ')
		blank = blank.split(' ')
		blank[num-1] = "X"
		chunks = [blank[x:x+self.columns] for x in xrange(0, len(blank), self.columns)]
		chunks = "\n".join(str(x) for x in chunks)
		blank = open('blank', 'w')
		blank.write(chunks)
		return chunks
		
	def high_scores(self, name, score):
		"""Records the high score in an appropriate file for storage
		   Assumes name is a string and score is an int.
		   Returns a file by board size containing the high scores"""
		num = str(score)
		score_handle = open(str(self.rows*self.columns), 'a')
		temp_file = score_handle.write(" "+name)
		temp_file = score_handle.write(" "+num)
		score_handle.close
		
	def read_scores(self, rows, columns):	
		if os.path.isfile(str(rows*columns)) == True:
			score_handle = open(str(rows*columns), 'r')
			temp_file = score_handle.read()
			temp_file = temp_file.split(" ")
			while len(temp_file) > 20:
				temp_file.pop(0)
				temp_file.pop(1)
			entry = {}
			m = 1
			n = 2
			for i in range(1, len(temp_file)-len(temp_file)/2):
				entry[temp_file[m]] = int(temp_file[n])
				m += 2
				n += 2
			import operator
			sorted_entry = sorted(entry.iteritems(), key=operator.itemgetter(1)) 
			for i in sorted_entry:
				print i[0]+":", "Score",i[1]
			return 
		else:
			return "Nobody has played that game yet."
			
	def save_game(self, name):
		os.rename('blank', name)
		os.rename('board', name+'1')
		return

	def load_game(self, name):
		if os.path.isfile(name) == True:
			os.rename(name, 'blank')
			os.rename(name+'1', 'board')
			return "Y"
		else:
			return "No file"

jim = memory_game(4,4)
#print jim.save_game("jerry")
print jim.load_game("jerry")
