#Brian Jansen
#Ex 24

#The following 15 lines or so we see print being used where escapes are demonstrated as well as \t and \n.  A poem is also assigned to the variable, poem.  It is then printed.
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend the passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "----"
print poem
print "----"

#Following line does math, and then prints it.
five = 10 - 2 + 3 - 6
print "This should be five: %d" % five #There was an error written on the actual page.  Dude used %s instead of %d

#The following 5 lines or so are a function that is defined where an argument is supplied and some math is done and then returned as 3 variables.
def secretformula(started):
	jellybeans = started * 500
	jars = jellybeans / 1000
	crates = jars / 100
	return jellybeans, jars, crates
	
#The following blocks print out the variables provided by calling the function and shows two different ways to express it within a print sequence.	
startpoint = 10000
beans, jars, crates = secretformula(startpoint) #Assigning three variables at a time?  That's pretty neat.

print "With a starting point of: %d" % startpoint
print "We'd have %d beans, %d jars, and %d crates." % (beans,jars,crates)

startpoint = startpoint/10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secretformula(startpoint) #Really like this
