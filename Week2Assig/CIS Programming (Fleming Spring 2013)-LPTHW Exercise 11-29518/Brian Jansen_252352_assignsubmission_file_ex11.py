# Brian Jansen
# Ex 11

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %s tall and %r heavy." % (age, height, weight)

# Played around with %r and %s a little more.  Strange that it adds the '' when you use %r, but when you use %s there are none.  Python is strange.

print "Do you like pizza?",
pizzalove = raw_input()
print "Oh...that's neat...Go away." 
