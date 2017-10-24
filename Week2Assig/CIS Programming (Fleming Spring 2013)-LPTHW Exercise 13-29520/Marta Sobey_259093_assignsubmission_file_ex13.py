#Marta Sobey
#Assignment Number 13. 2/10/14

#This will import information from different locations.
from sys import argv
#says the variable name of the arguments that will be used and the number of arguments that there are going to be. 
script, first, second, third, fourth = argv
#I added this for study drill number 3. It prints what is inside quotes prompting the user to respond
number = raw_input("What number do you choose?")

#Prints what is inside quotes followed by the content of the different variables which are assigned by the user when they insert them into shell. 
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your choice is:", number

#The error says I did not give it enough arguments to complete the script
#Study drill number 2 simply changes how many outputs you get.
