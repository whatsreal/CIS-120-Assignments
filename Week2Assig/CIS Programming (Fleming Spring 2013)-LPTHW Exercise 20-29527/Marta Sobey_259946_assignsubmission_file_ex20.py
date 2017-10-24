#Marta Sobey
#Assignment Number 20. 2/10/14

#This will import information from different locations.
from sys import argv
#denotes what arguments are going to be used.
script, input_file = argv

#defines print_all
def print_all(f):
	print f.read() #reading the 'f' file
	
def rewind(f): #take back to top
	f.seek(0) #seeking for position 0
	
def print_a_line(line_count, f): #print out line number and then prints the line
	print line_count, f.readline() #number and then reading that line of file 'f'

current_file = open(input_file) #assigning a variable

print "First let's print the whole file:\n" #printing what is inside quotes followed by a new line

print_all(current_file) #executing print_all function

print "Now let's rewind, kind of like a tape." #prints what is inside quotes

rewind(current_file) #back to top of current_file

print "Let's print three lines:" #prints what is inside quotes

current_line = 1 #assigning a variable
print_a_line(current_line, current_file) #prints the line number and then prints that line from current_file

current_line = current_line + 1 #adding one to a variable
print_a_line(current_line, current_file) #same as line 32

current_line = current_line + 1 #same as line 34
print_a_line(current_line, current_file) #same as line 32

#from the definition in line 16, the variable line_count become current_line in line 32
# += adds to a current variable