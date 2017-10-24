#Elizabeth Murg
#Assignment Number 20. 2/8/2014

#line 5 we are telling the program what plan to use
from sys import argv

#then we define and unpack our args
script, input_file = argv

#in line 11 we define a new function called print_all which will read our file 
#it has the argument f which stands for file
def print_all (f):
	print f.read()

#Anytime you use f.seek basically you're going back to the beginning of the file (or wherever you specify in the parantheses)
def rewind(f):
	f.seek(0)

#Here you are telling the program to count the amount of lines in the input_file
def print_a_line (line_count, f):
	print line_count, f.readline()

#At line 24 we define a new variable to be current_file and this will tell the program to open the input_file so we can make changes
current_file = open(input_file)

#This line is telling the user what the program does first (\n means it is written on a new line)
print "First let's print the whole file: \n"

#now we tell our function print_all that it's new argument is current_file and so the function will do what current_file says: open the file
print_all (current_file)

#Now in line 33 the program tells the user that it is going back through the file
#and gives the rewind function a new argument as well: current_file which will open the file and then go back through it 
print "Now let's rewind, kind of like a tape."

rewind(current_file)

#Next, the program will print only three lines of the document
print "Let's print three lines:"

#Here we are just going to be telling the program what lines to print and some numbers to print for each line :)
current_line = 1
print_a_line (current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#Study Drill 4. the seek function will move back to the start of the file or whatever byte you specify
#Study Drill 5. Basically writing variable += a number is the same as writing variable = variable + number
#Study Drill 2. So. print_a_line is defined as having two arguments: the line count and f (which stands for file)
#When we call for the function in line 27 we change the names to current_line which we gave as a variable to be number 1: and since we are at the beginning of the file anyways it's perfect.
#That takes care of line_count. Then, f is replaced with current_file which will open the input_file and read it too (print it to the screen).
