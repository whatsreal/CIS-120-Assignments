#Mason Hunter CIS 120
#Assignment 38
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, elt's fix that."

stuff = ten_things.split(' ') #splitting up that ten things variable
more_stuff = ["Day", "night", "song", "Frisbee", "corn", "Banana", "girl", "Boy"] #making a list

while len(stuff) != 10:#this gets the length of ten things to ten by adding things from other stuff
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)
    
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #prints second thing off stuff list
print stuff[-1] #prints last thing off stuff
print stuff.pop()
print ' '.join(stuff) #lists out individually the things from stuff
print '#'.join(stuff[3:5]) #slices out telephone and adds it to list

# SD 5: dir tells you about the attributes of something, and class is one of those attributes (I think)