# Justin Small, Excersise 16, 2/9/2014

#from sys import argv

#script, filename = argv

filename = raw_input()

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
bullseye = open(filename, 'r')

#print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
lines = (line1, line2, line3)

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#print "And finally, we close it."
target.close()

print "And now we'll open it."
print bullseye.read()

#Study Drills
#1. I understand this already
#2. Check ;)
#3. Not quite sure how I could do this.
#4. We much use 'w' to open a file so that python know what to expect us to do with the file we just opened
#5. No we do not need the truncate function in order to write to this file. Only if we want to re-write it.
