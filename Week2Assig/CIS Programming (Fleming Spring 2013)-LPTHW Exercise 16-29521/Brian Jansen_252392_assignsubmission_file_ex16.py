#Brian Jansen
#Ex 16

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#That W up there opens the file to be written and no, it would not need that W to be truncated

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#I wrote the following line when I was copying the script.  Guess I saved myself some time in the study drills.
target.write("%s\n%s\n%s" % (line1, line2, line3)) 
target.close()

raw_input("Would you like to check %s?" % filename)
target = open(filename)
stuff = target.read()
print stuff
raw_input("...")
print "And finally, we close it."
target.close()

