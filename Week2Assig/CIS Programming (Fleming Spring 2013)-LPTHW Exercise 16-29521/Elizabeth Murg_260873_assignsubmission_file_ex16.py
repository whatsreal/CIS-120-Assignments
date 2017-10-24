#Elizabeth Murg
#Assignment Number 16. 2/6/2014.

#This tells the computer what plan to use
from sys import argv

#This line describes what arguments will be used and unpacks them
script, filename = argv

#These lines will tell the user what the program wants to do through a string
#It will use the format character %r and the argument filename to say which file it will act upon
print "We're going to erase %r." %filename
#These next two lines will give the user two options for what they want the program to do next (using two commands)
print "If you don't want that hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#this line will define the prompt symbol for the user 
raw_input ("?")

#This line will tell the user what the program is doing next and give the command to open the file and write in it
print "Opening the file..."
target = open(filename, 'w')

#This line will explain to the user that the computer is now going to delete what is in the file
print "Truncating the file. Goodbye!"
target.truncate()

#This line tells the user to imput three lines
print "Now I'm going to ask you for three lines."

#These are where the user must input the next lines
line1 = raw_input ("line 1: ")
line2 = raw_input ("line 2: ")
line3 = raw_input ("line 3: ")

#The program will now inform the user that it will write these lines in the file
print "I'm going to write these to the file."

#This next blook will write the lines inputted by the user each into a new line in the document
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# new way to write lines without having so many lines
allinone = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write (allinone)

#This line informs the user that the program will now be closed and the next line performs the action
print "And finally, we close it."
target.close

#Study Drill 4. Aside from actually telling the computer we want to write in the file we are also creating the file in the same command.
#Study Drill 5. Truncating the file is really not necessary at all once you've opened it in write mode which will overwrite the file