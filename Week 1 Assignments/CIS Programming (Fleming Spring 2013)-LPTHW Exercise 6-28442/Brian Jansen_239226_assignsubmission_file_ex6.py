#Brian Jansen
#Ex 6

#The following lines are variables where the values are strings.  Throughout the values, there are also other variables or numbers thrown in, in a needlessly complicated way to help students understand...
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#In the lines below, the values of the variables x and y are printed
print x
print y

#more printing....
print "I said: %r." % x
print "I also said: '%s'." % y

#Variables with strings that the author uses to say he's not funny
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#he prints the above variables.
print joke_evaluation % hilarious

#Variables w and e are made with a string
w = "This is the left side of..."
e = "a string with a right side."

#the two strings are combined and printed with a plus symbol
print w + e

#Not sure what he means by putting a string inside another...if he considers the line above as doing that, then there would be five.
