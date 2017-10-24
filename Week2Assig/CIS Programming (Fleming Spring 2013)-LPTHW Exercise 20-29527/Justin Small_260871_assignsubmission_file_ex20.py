# Justin Small, Excersise 20, 2/9/2014

#This line imports the argv module from the system
 from sys import argv

#This line sets argv equal to the script and another input file
script, input_file = argv
#I added this line in order to run the file within the interpreter 
#input_file = raw_input()

#This line sets the function print_all(f):
def print_all(f):
	#This line specifies that print_all(f) will print the reading of of a file
    print f.read()

#This line sets the function rewind(f): 
def rewind(f):
	#This line specifies that rewind(f) will seek point zero within a file
    f.seek(0)

#This line sets the function print_a_line with arguements (line_count, f):
def print_a_line(line_count, f):
	#This line specifies that print_a_line will print the line_count of a particular file.
    print line_count, f.readline(),

#This line tells the variable current_file to open the input_file
current_file = open(input_file)

#This line tells us what the program is doing
print "First let's print the whole file:\n"

#This line calls the function print_all and assigns the variable current_file
print_all(current_file)

#This line tells us what the program is doing
print "Now let's rewind, kind of like a tape."

#This line calls the function rewind and assings the variable current_file
rewind(current_file)

#This line explains what the program is doing
print "Let's print three lines:"

#This line assigns the arguement current_line a value of 1
line_count = 1 
#This line calls the function print_a_line and assigns in the arguements current_line and current_file
print_a_line(line_count, current_file)

#This line assigns the arguement current_line a value of current_line + 1 
line_count += 1 
#This line calls the function print_a_line and assigns it the arguements current_line and current_file
print_a_line(line_count, current_file)

#This line assings the arguement current_line a value of current_line + 1
line_count += 1
#This line calls the function print_a_line and assigns it the arguements current_line and current_file
print_a_line(line_count, current_file)

#Study Drills
#1. Done
#2. #current line is equal to the value of 1, then the curent line plus one more, and lastly the current line plus one more. It is passed to print a line because it is the substitue for "line_count" in that function.
#3. All the functions should have the right arguements
#4. I did both of these things
#5. I did it
