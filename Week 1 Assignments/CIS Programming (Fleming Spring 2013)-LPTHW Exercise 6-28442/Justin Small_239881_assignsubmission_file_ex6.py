# Justin Small 1/25/2013

# this line enstantiates variable x as "There are %d types of people." and then defines % as 10
x = "There are %d types of people." % 10 # (string within a string)
# this line enstantiates variable binary as the word "binary" 
binary = "binary"
# this line enstantiates variable do_not as the word "don't"
do_not = "don't"
# this line enstatiates variable y and the string "Those who %s binary and those who %s, and then deifnes % as the list (binary, do_not)
y = "Those who %s binary and those who %s." (binary, do_not) # (2 strings within a string)

# this line prints variable x 
print x
# this line prints variable y 
print y

# this line prints the words "I said: %r." with % equal to variable x
print "I said: %r." % x
# thie line prints the words "I also said" '%s'." with % equal to variable y 
print "I also said: '%s'." % y

# this line enstantiates variable halarious as the quantity False
hilarious = False
# this line enstantiates variable joke_evaluation as the words "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r" # (string within a string)

# this line prints the varable joke evaluation followed by the embedded string halarious.
print joke_evaluation % hilarious

# this line enstantiates variable w as the string "This is the left side of..."
w = "This is the left side of..."
# this line enstantiates variable e as the string "a string with a right side."
e = "a string with a right side."

# this line prints the result of adding variable w to variable e
print w + e
# this is a long string because a string plus a string equals a longer string. 