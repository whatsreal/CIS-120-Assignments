#Marta Sobey
#Assignment Number 11. 2/10/14

#These lines print what are inside the quotes followed by a place for the user to respond to the questions asked. The answers are then assigned the specific variables (age, height, or weight)
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#Prints what is inside quotes while replacing the %r characters with the stored input from the variables age, height, and weight respectively.
print "so, you're %r old, %r tall and %r heavy." % (age, height, weight)

# raw_input allows the user to interact with a program by directly typing in the responses they want printed.

#Example from online
#These lines print what is in either single quotes or double quotes followed by an apportunity for the user to input their own responses.
name = raw_input ('Enter your name : ')
#Prints what is in quotes, but replaces %s with the information stored under the variable 'name'
print ("Hi %s, Let us be friends!" % name);

#My version of the code above. I am asking questions and giving the user the ability to respond
print "What year were you born?",
born = raw_input()
print "How many people are in your immediate family?",
family = raw_input()
print "What is your favorite number?",
number = raw_input()
#printing out the user's responses
print born
print family
print number
#The first line prints what is inside quotes. The comma tells shell to print the next line started from the spot the last line left off and not to make a new line. 
print "Your number is... ",
#This line adds the integer value of the variables together and prints them.
print born+family+number

#The backslash in the height has to be there since each number in that string is inside single quotes, the backslash needs to be inserted to show that that is not the end of the quote and it is just being used as a symbol for feet.

