
# Justin Small, Excersise 15, 2/9/2014 "Check in computer lab"

# This line imports the module argv from the system.
#from sys import argv

#this assigns the arguments for argv
#script, filename = argv
filename = raw_input() 

#this tells python to open the txt file
txt = open(filename)

#This line prints here's your file and gives the filename
print "Here's your file %r:" % filename
#this line prints the text contained in the file
print txt.read()

close(filename)
#this line prompts the user to enter the filename again
#print "Type the filename again:"
#this line tells python the name of the file you want to open
#file_again = raw_input("> ")

#this line opens that file
#txt_again = open(file_again)

#this line prints the text containted within that file
#print txt_again.read()

#Study Drills
#1. I have inserted all comments
#2. I know what everything does
#3. I couldn't quite find any other definitions
#4. It causes the program to no longer ask for my to repeat the filename.
#5. It first opens the file and then asks for the file name within python instead of from command line. I can't think of why one method would be better than another.
#6. Did it. It was weird and didn't work
#7. I don't. This is a little too complicated
#8. OK