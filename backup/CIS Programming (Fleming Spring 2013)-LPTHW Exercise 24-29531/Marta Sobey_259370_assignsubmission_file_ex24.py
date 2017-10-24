#Marta Sobey
#Assignment Number 24. 2/10/14

#prints what is inside quotes using escape sequences to say when they want the strings on different lines.
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\that do \n newlines and \t tabs.'

#Prints what is inside the triple quotes using commands to tab and start different lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#prints what is inside quotes
print "--------------"
#prints the content that the variable 'poem' entails
print poem
print "--------------"

#assigns the variable 'five' with the answer to the math following the = symbol
five = 10 - 2 + 3 - 6
#prints what is inside quotes while replacing %s with the content of variable five
print "This should be five: %s" % five

#defines variables
def secret_formula(started):
	jelly_beans = started * 500
jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#prints what is in quotes while replacing %d with the content of the respective variables start_point, beans, jars, abd crates.
print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#re-defines the variable start_point
start_point = start_point / 10

#prints what is inside quotes while replacing %d with the content of the respective variable
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#error on line 25 is an indentation error