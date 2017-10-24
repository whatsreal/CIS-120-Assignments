#Elizabeth Murg
#Assignment Number 6. 1/27/14

# This line creates the variable "x" to be a sentence. Inside the sentence the format character %d functions as a replacement for "10"
x = "There are %d types of people." % 10
# This line defines the variable binary to be the word "binary"
binary = "binary"
#This line creates a variable do_not for the word "don't"
do_not = "don't"
#This line also creates a variable "y" for another sentence. Using the format characters for string variables it also causes %s to be replaced with two words
y = "Those who know %s and those who %s." % (binary, do_not) # This is one place where a string is put inside a string (#1)

# This line tells the computer to print the sentence defined for variable "x".
print x
# This line tells the computer to print the sentence defined for variable "y".
print y

#This line gives the command to print whatever is between quotations while also replacing the format character for string variable with what is defined for variable "x"
print "I said: %r." % x #This is another spot where a string is inside another string (#2) 
#This line also gives the command to print whatever is between quotations while also replacing the format character for string variable with what is defined for variable "y"
print "I also said: '%s'." % y #This is another location where a string is printed inside a string (#3)

#This line defines the variable hilarious to be False
hilarious = False
#This line creates a new variable called joke_evaluation and also adds the %r format character 
joke_evaluation = "Isn't that joke so funny?! %r" #This is the fourth location where a string is printed inside a string (#4)

#This line commands the computer to print the variable for joke_evaluation and hilarious to replace the %r in the joke_evaluation variable
print joke_evaluation % hilarious

#This line defines a new variable under the name "w"
w = "This is the left side of..."
#This line creates a new variable under the name "e"
e = "a string with a right side."

#This line tells the computer to print the two variables on the same line
print w + e

#There are only four locations where a string is inside a string and you can tell because of the format characters %r and %s which are used for string variables. 
#When %r and %s are inside quotation marks, that is a string placed inside a string

#Adding the two strings "w" and "e" together with a + obviously makes a longer string because you are combing two shorter strings into one longer one
