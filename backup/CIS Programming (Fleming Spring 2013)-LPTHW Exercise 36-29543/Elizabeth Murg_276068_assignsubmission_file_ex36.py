#Elizabeth Murg	
#Assignment Number 36. 2.15.2014.

from sys import exit

def zebra():
    print "This room is full of zebras."
    print "Do you want the purple zebra, the dying zebra, or the fierce zebra?"
    
	
    next = raw_input ("> ")
    if "purple zebra" in next:
		print "Good choice! You win!"
		exit(0)
    if "dying zebra" in next:
		print "Umm...and why???"
		dead ("You lose.")
    if "fierce zebra" in next:
		print "The fierce zebra tramples you to death."
		dead ("You lose.")

def monkeys ():
	print "This room is full of monkeys blocking a door."
	print "What do you do?"
	monkey_moved = False
	
	while True:
		next = raw_input ("> ")
		
		if next == "scream": 
			dead ("The monkeys kill you.")
		elif next == "give banana" and not monkey_moved:
			print "The monkeys have gone away!"
			monkey_moved = True
		elif next == "give banana" and monkey_moved:
			print "The monkeys demand even more."
			dead ("You are stuck here forever.")
		elif next == "open door" and monkey_moved:
			zebra ()
		else: print "You can only scream or give banana to the monkeys before you open the door."
def poop ():
	print "Here is a room full of dung."
	print "The smell is overpowering. Do you flee or stay to clean?"
	
	next = raw_input ("> ")
	
	if "flee" in next:
		start()
	if "stay" in next:
		print "You are a trooper. You discover a gold mine. You win!"
		exit(0)
def dead (why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a zoo."
	print "There are only two rooms. One to the left, one to the right."
	print "Which do you take?"
	
	next = raw_input ("> ")
	
	if next == "left":
		poop()
	elif next == "right":
		monkeys ()
	else:
		dead ("Fine, stay here forever.")
start()
	