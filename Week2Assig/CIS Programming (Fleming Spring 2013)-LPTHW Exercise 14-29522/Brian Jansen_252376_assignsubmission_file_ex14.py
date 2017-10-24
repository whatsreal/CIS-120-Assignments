#Brian Jansen
#Ex 14
#Study Drills are commented out...

from sys import argv

script, user_name = argv
#script, real_name, user_name = argv 

prompt = "> "
#prompt = "Respond... "

print "Hi %s, I'm the %s script." % (user_name, script)
#print "Hi %s, I'm the %s script.  Can I call you %s?" % (real_name, script, user_name)
#raw_input(prompt)
#print "Neato, I will, %s" % user_name
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
