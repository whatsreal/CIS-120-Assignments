#Marta Sobey
#Assignment Number 17. 2/10/14

#This will import information from different locations.
from sys import argv
#checks to see if a file exists at this point
from os.path import exists
#denotes what arguments are going to be used.
script, from_file, to_file = argv
#prints what is in quotes replacing the %s characters with what the user specifies as the from_file and to_file
#print "Copying from %s to %s" % (from_file, to_file)

#We could do these two on one line too, how?
#assigns the variable in-file to the data which opens the from_file. assigns the variable indata to the data which is reading the content of in_file
in_file = open(from_file) ; indata = in_file.read()

#prints what is in quotes replacing %d with the value of len(indata) which is the length of the indata
#print "The input file is %d bytes long" % len(indata)

#prints what is in quotes and asks the user to respond
#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

#assigns the variable out-file to the data which opens the to_file. Write the data from indata into the out_file
out_file = open(to_file, 'w') ; out_file.write(indata)

#print what is in quotes
#print "Alright, all done."
#closes the two files
out_file.close() ; in_file.close()

# I was able to import some of my previous python files
# Adding semicolons allows you to put everything on one line
# Con Cat: "Synopsis Gets the content of the item at the specified location."
# You want to output.close() because you should always close files when you are done with them.