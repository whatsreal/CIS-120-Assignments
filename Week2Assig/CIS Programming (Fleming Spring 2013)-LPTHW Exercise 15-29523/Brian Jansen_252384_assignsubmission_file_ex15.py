#Brian Jansen
#Ex 15

#The following two lines loads the argv module then it gives variables involved their values
from sys import argv
script, filename = argv

#The following lines opens up the file specified in the argv variable, then it prints the name, and then prints the contents
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()

#The lines below use the raw_input function to ask you a file name and then loads the text from the file you specify and prints it.
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
