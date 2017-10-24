#Marta Sobey
#Assignment Number 16. 2/10/14

#This will import information from different locations.
from sys import argv
#denotes what arguments are going to be used
script, filename = argv

#Prints what is inside quotes but replaces %r with the file name the user inserts into shell.
print "We're going to erase %r." % filename
#Prints what is inside quotes as is.
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#Prints a question mark as a prompt for the user to import data.
raw_input("?")

#Prints what is in quotes. Opens a file with the given name for writing. 
print "Opening the file..."
#Opens the file 'target' for writing
target = open(filename, 'w')

#Prints what is in quotes. 
print "Truncating the file. Goodbye!"
target.truncate()
#Prints what is in quotes.
print "Now I'm going to ask you for three lines."
#The user inserts their own lines which are assigned to the variables line1, line2, and line3
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#Prints what is in quotes
print "I'm going to write these to the file."
#Writes line1, line2, and line3 on different lines from the file
target.write(line1 +"\n"+ line2 +"\n"+ line3)
#Tells shell to go to a different line
#target.write("\n")
#Writes line2 from the file
#target.write(line2)
#Tells shell to go to a different line
#target.write("\n")
#Writes line3 from the file
#target.write(line3)
#Tells shell to go to a different line
#target.write("\n")
#Prints what is in quotes
print "And finally, we close it."
#Closes the file
target.close()
#open the file
#target = open(filename)
#print filename.read()
#The 'w' tells you that you want to open the file to write mode
#You don't need it because you are in writing mode and truncating is for reading.