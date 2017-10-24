#Elizabeth Murg	
#Assignment Number 17. 2/6/2014.

#These lines will tell the computer what program to use
from sys import argv
from os.path import exists

#this line defines the arguments
script, from_file, to_file = argv

#This line will tell the user what the program will do (copy one file from one to another)
print "Copying from %s to %s" % (from_file, to_file)
#This line creates a new variable for the command opening the first file
in_file = open(from_file)
#This line creates a new variable for the variable we just created to read the file we just opened in  the last variable
indata = in_file.read()

#This line will tell us how long the file is that we just opened and read
print "The input file is %d bytes long" %len(indata)

#These next lines will let the user know if the file exists that we want to copy to
#Then, the user has the option (using raw_input) to know if to continue or stop
print "Does the output file exist? %r" % exists (to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#These next lines will create a new variable called the out_file which uses the command to open the file we are copying to 
#And then using the variable we tell the program to whatever was in the from_file to the to_file
out_file = open(to_file, 'w')
out_file.write(indata)

#Finally we let the user know that the copying is done
print "Alright, all done."

#And we close both files :)
out_file.close()
in_file.close()

#Study Drill 5, I'm pretty sure the Linux/OSX people use cat too. That's all I could find online
#Study Drill 6, because Python doesn't necessarily close it for you. Also, some systems won't let the same file be opened at the same time to read and write 
