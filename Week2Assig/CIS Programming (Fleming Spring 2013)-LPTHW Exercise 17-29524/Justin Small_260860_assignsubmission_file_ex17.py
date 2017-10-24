# Justin Small, Excersise 17, 2/9/2014

import modulefinder 
from sys import argv
from os.path import exists

#script, from_file, to_file = argv
from_file = raw_input()
to_file = raw_input()

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

#Study Drills
#1. I read the statement but can't quite figure it out yet.
#2. I removed some of the extraneous strings 
#3. I'm trying my best. I couldn't figure this out.
#4. Okay. I found no information on cat
#5. I don't know how to find an alternative because I can't find any information on cat.
#6. I had to do this so that the file could no longer be red or written.
