# Justin Small, Exercise 38, 2/16/2014

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # this allows ten_things to be edited
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #this pops something out of more_stuff and assigns it to next_one
    print "Adding: ", next_one
    stuff.append(next_one) # this basically appends stuff by adding next one to it.
    print "There's %d items now." % len(stuff) #this gives the number of things in stuff

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop() # this is basically pop(stuff) 
print ' '.join(stuff) # what? cool! this is basically join(' ', stuff). It joins the things in stuff with' '
print '#'.join(stuff[3:5]) # super stellar! this is basically join("#", stuff[3:5]). It joins 3:5 with a #

# Study Drills:
#1. yep :)
#2. Ouch, imma try. 
#3. 
