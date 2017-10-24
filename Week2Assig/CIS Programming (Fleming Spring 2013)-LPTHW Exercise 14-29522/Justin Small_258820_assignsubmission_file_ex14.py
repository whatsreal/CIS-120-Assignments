# Justin Small, Excersis 14, 2/9/2014 "Check in Computer lab"

from sys import argv

script, user_name, number = argv
prompt = "* "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Why did you pick %s?" % number
reason = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
You picked number %r because %r
And you have a %r computer.  Nice.
""" % (likes, lives, number, reason, computer)

#Study Drills
#1. Zork and Adventure
#2. Done and Done
#3. Yup
#4. Check
