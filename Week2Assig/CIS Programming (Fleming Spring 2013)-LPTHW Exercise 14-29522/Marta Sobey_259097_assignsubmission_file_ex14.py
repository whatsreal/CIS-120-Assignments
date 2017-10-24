#Marta Sobey
#Assignment Number 14. 2/10/14

#This will import information from different locations.
from sys import argv

#Denotes what arguments are going to be used.
script, user_name = argv
#Specifies what is going to prompt the user to insert their own information
prompt = 'Type Response Now...'

#Prints what is inside quotes while replacing the %s characters with their respective variables listed in parentheses. They also give the user the opportunity to respond to the questions asks.
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#Assigns the input inserted a variable name of 'likes'
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
#Assigns the input inserted a variable name of 'lives'
lives = raw_input(prompt)

print "What kind of computer do you have?"
#Assigns the input inserted a variable name of 'computer'
computer = raw_input(prompt)

print "What is your favorite sport?" 
#Assigns the input inserted a variable name of 'sport'
sport = raw_input(prompt)

#Prints what is inside quotes while replacing the %s characters with their respective variables listed in parentheses.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
I like your favorite sport, %r, too.
""" % (likes, lives, computer, sport)

#Zork and Adventure was the first computer game ever made available to the general public.
#I changed my prompt variable to 'Type Response Now..."
#I added the argument 'sport'
#Combining these two symbols does not change how they work. 