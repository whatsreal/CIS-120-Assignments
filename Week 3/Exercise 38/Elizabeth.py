#Elizabeth Murg
#Assignment Number 38. 2/17/2014.

#first he made a variable of a string of 6 words
ten_things = "Apples Oranges Crows Telephone Light Sugar"

#this will print to screen
print "Wait there's not 10 things in that list, let's fix that."

#then he made a new variable which will split the string into individual words.
stuff = ten_things.split (' ')
#then he makes  list with more words
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#using a while loop he says that while the len of stuff is not equal to ten, the program should pop off an item from more_stuff and add it to stuff
while len(stuff) != 10:
	next_one = more_stuff.pop()
	#then the program will print what it just popped off the top
	print "Adding: ", next_one
	#then it will add it to stuff using append
	stuff.append(next_one)
	#then using format character %d and the length it will tell us how long our lsit is
	print "There's %d items now." % len(stuff)

#then it will print the new list
print "There we go: ", stuff

print "Let's do some things with stuff."

#this block will first show the 2nd item on the list, then the last then it will pop the first one of the list, then it will show the list individually separated by a space, and finally it will join the fourth and the sixth item on the list with a # sign. 
print stuff[1]
print stuff[-1] # whoa! fancy!
print stuff.pop()
print ' '.join(stuff) #what? cool!
print '#'. join(stuff[3:5]) #superstellar!

#couldn't figure out how to do study drill 1. 