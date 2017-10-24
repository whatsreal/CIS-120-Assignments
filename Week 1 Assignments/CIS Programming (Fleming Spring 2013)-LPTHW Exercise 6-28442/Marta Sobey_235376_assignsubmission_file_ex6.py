#Marta Sobey
#Assignment number 6. 1/27/2014

#The variable 'x' is being assigned the string 'There are %d types of people." where %d is assigned the value of 10.
x = "There are %d types of people." % 10
#The variable 'binary' is assigned the string "binary"
binary = "binary"
#The variable 'do_not' is assigned the string "don't"
do_not = "don't"
#The variable 'y' is assigned the string "Those who know %s and those who %s." where the first %s is assigned the contents of the variable 'binary' and the second %s is assigned the contents of the variable 'do_not'
y = "Those who know %s and those who %s." % (binary, do_not)
#This line is going to print the contents of the variable 'x' as described above.
print x
#This line is going to print the contents of the variable 'y' as described above.
print y
#This line is going to print "I said: %r." where %r refers to the content of the variable 'x'
print "I said: %r." % x
#This line is going to print "I also said: '%s'." where %s refers to the content of the variable 'y'
print "I also said: '%s'." % y
#The variable 'hilarious' is assigned the response 'False'.
hilarioius = False
#The variable 'joke_evaluation' is assigned the string "isn't that joke so funny?! %r" where %r will refer to another variable's content
joke_evaluation = "Isn't that joke so funny?! %r"
#This line prints the contents of the variable 'joke_evaluation' followed by the response that was assigned to the variable 'hilarious'
print joke_evaluation % hilarioius
#The variable 'w' is assigned the string "This is the left side of..."
w = "This is the left side of..."
#The variable 'e' is assigned the string "a string with a right side."
e = "a string with a right side."
#This line prints the contents of the variable 'w' directly followed on the same line by the contents of the variable 'e'
print w + e