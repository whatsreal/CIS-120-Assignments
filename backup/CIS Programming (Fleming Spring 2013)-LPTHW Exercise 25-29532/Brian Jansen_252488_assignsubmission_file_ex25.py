#Brian Jansen
#Ex 25

def breakwords(stuff):
	words = stuff.split(' ')
	return words
	
def sortwords(words):
	return sorted(words)
#I hate when the author does this ^^

def printfirstword(words):
	words = words.pop(0)
	print word
	
def printlastword(words):
	word = words.pop(-1)
	return word
	
def sortsentence(sentence):
	words = breakwords(sentence)
	return sortwords(words)
	
def printfirstandlast(sentence):
	words = breakwords(sentence)
	printfirstword(words)
	printlastword(words)
	
def printfirstandlastsorted(sentence):
	words = sortsentence(sentence)
	printfirstword(words)
	printlastword(words)

#Hmm, it seems I neglected the documentation comments.  Oops.  I'm really digging the help function for modules and how it's automatically generated.
#The more we do in python, the more I like some of it's neat little tricks.  
	

