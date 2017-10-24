# Justin Small, Exercise 36, 2/16/2014

from sys import exit

def bedroom3():
	print "Welcome to the bedroom"	


def bathroom2():
	print "Welcome to the bathroom"


def livingroom():
	print "Welcome to the living room"

	
def	goodbye(why):
	print why, "Goodbye."
	exit(0)

	
def frontdoor():
	print "Welcome to my house!"
	print "Would you like to come in and meet my family?"
	
	reply = raw_input("> ")
	
	if reply == "yes":
		livingroom()
	else:
		goodbye("Okay, have a nice day.")
		
frontdoor()
	
# AHHHHH I NEED MORE TIME!!!!
		
	
