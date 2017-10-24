#Elizabeth Murg
#Assignment Number 14. 2/5/2014.

#this line tells python what plan to use
from sys import argv

#line 9 will define the arg and unpack them
#thegirl is my new arg
script, user_name, thegirl = argv
#I change the prompt from '>' to ':)'
#this line will define the prompt so that Python will give it everytime
prompt = ':)'

#this will form strings which will print out whatever is set to the arg
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
#this line will ask the user to answer a question about one of the variables. the answer will be assigned to the variable likes
print "Do you like me %s?" % user_name
likes= raw_input(prompt)

# in lines 22 through 30 the user is asked to answer a question and his question is assigned to a specific variable using raw_input
print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

#I added this new sentence using my new arg
print "Is %s the mathematics major?" % thegirl
happy = raw_input (prompt)

#this line combines the answers of the user into one long string using the format characters %r and %s
print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice. And %s Betty IS the math major. Cool!
""" % (likes, lives, computer, happy)

#tried playing zork online for free at http://freebies.about.com/od/onlinegames/p/how-to-play-zork.htm
#weird game...with only text so all the graphics would technically be your imagination
#it's really opaque and you don't know what to type in because they don't explain
