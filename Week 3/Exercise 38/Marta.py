#Marta Sobey 
#Assignment Number 38. 2/17/14

#assigns a variable to a string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."
#split(' ', ten_things)
#ten_things.split(' ') reads as, "split ten_things with ' ' between them." Meanwhile, split(' ', ten_things) means, "Call split with ' ' and ten_things."
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#prompts a while loop with a parameter of length of a list does not equal 10
while len(stuff) != 10:
	#.pop takes the last thing off the end of the list first.
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	#append adds a new value to the end of a list
	stuff.append(next_one)
	#len() is the length of a certain string or list
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #whoa! fancy
print stuff.pop()
print ' '.join(stuff) #what? cool!
print '#'.join(stuff[3:5]) #super stellar!

#OOP is a design philosophy
#classes are created at runtime and can be modified further after creation
#class dir is inheriting from the class something
