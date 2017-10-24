#Elizabeth Murg
#Assignment Number 15. 2/5/2014.

#This line tells Python what plan to use and which module to import
#from sys import argv

#This line defines the arguments and unpacks them
#script, filename = argv

#This line calls for a new command "open" to open one of the arg
#txt = open (filename)

#This line creates a string which then inputs the arg "filename" using the format character %r
#print "Here's your file %r:" % filename 
#This file has a command to display the file txt
#print txt.read()

#This line gives a string and then the line underneath uses raw_input to ask the user to answer the prompt in the string
print "Type the filename again:"
file_again = raw_input (">")

#This line gives the command to open whatever file the user gave in the file_again raw_input part
txt_again = open (file_again)

#Once again this is a command to read whatever is in the file (print it on the screen).
print txt_again.read()

#Study Drill 3 are class and toolbox other names for functions?
#Study Drill 4,5 I think the better way is the first one because you don't have to type in the filename again. But i'm not sure because there seems to be no big difference. 
#Can't get pydoc file to work... Not sure what is wrong?