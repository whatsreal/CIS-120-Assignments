#Elizabeth Murg
#Assignment Number 12. 5/5/2014.

#This is basically the same thing as in ex11 except now the prompt and the raw_input are on the same line.
#the prompt asks for the user to input an answer in this block using raw_input
age = raw_input ("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input ("How much do you weight? ")

#this block has a response to the inputs in the form of a string using the answers linked to the variables
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#when I type in either the words "pydoc raw_input" or "-m pydoc raw_input" (withouth quotation marks) I only get an error message
#I tried it in my folder and in the home area but I only get the error that -m and pydoc are not recognized as the name of a cmdlet, function, script file, or operable spelling
# The pydoc module should technically find documentation from Python modules
