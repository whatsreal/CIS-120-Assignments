#Brian Jansen
#Ex20

#Module import...
from sys import argv
script, input_file = argv

#Makes a function to print the contents of a file
def print_all(f):
	print f.read()

#function to take the file back to the start.  Basically making another version of seek with a different name...
def rewind(f):
	f.seek(0)

#prints the file line by line while also including the number that is specified through the linecount variable
def print_a_line(linecount,f):
	print linecount, f.readline()
	
#Opens a file for reading
current_file = open(input_file)

#Calls the print_all function with the current_file variable
print "First, let's print the whole file:\n"
print_all(current_file)

#Calls the rewind function with the current_file variable
print "Now, let's rewind."
rewind(current_file)

print "Let's print three lines:"

#calls the print_a_line function to read the file line by line while also including line numbers....
current_line = 1
print_a_line(current_line,current_file)
current_line += 1                            
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line,current_file)
