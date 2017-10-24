#Brian Jansen
#Ex 38

tenthings = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list.  Let's fix that..."

stuff = tenthings.split(" ") #split(tenthings, " ")
morestuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	nextone = morestuff.pop()
	print "Adding: ", nextone
	stuff.append(nextone) #append(stuff, nextone)
	print "There's now %d items." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff) #join(" ", stuff)
print "#".join(stuff[3:5]) #join("#", stuff)
#dir() lists objects within the program.
