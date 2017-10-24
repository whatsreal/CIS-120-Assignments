#Marta Sobey
#Assignment Number 15. 2/10/14

#This will import information from different locations.
from sys import argv

#denotes what arguments are going to be used.
#script, filename = argv
filename = raw_input("What is your file name?")
#this opens a file
txt = open(filename)
#This line prints the line in quotes, but replaces the %r with the file name which is ex15_sample.txt

print "Here's your file %r:" %filename

#This line reads the text that is in the .txt file which was called on.
print txt.read()
#This line prints the words that are in quotes as is.
print "Type the filename again:"
#This line prompts the user to type the file name again with a > symbol.
file_again = raw_input("> ")

#This line prompts shell to open the .txt file that the user inserted into shell in the previous line.
txt_again = open(file_again)
#This line prints the content in the .txt file that the user prompted shell to open.
print txt_again.read()

txt_again.close()
txt.close()
#I did not find much information on python open. All I found was that it is used to open files
#Most definitions referred to commands as functions online.
#Using the raw_input requires the user to know more
#For study drill number 6 some other commands I can use include close(), fileno(), flush()...
#I opened files from pydoc and rand .read on them
