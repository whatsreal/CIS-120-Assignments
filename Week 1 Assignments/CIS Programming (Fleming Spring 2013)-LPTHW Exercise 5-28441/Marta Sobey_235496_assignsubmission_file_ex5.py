#Marta Sobey
#Assignment number 5. 1/27/2014

name = 'Zed A. Shaw'
print "Let's talk about %r." % name
height = 74 # inches
print "He's %r inches tall." % height
weight = 180 # lbs
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
hair = 'Brown'
eyes = 'Blue'
print "He's got %r eyes and %r hair." % (eyes, hair)
teeth = 'White'
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
age + height + weight
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)

inches = 2.54 #centimeters
kilo = 2.20 #pounds
#This line means that this command is going to convert 12 inches to the appropriate number of centimeters.
print "12 inches =", 12 * inches, 'centimeters'
#This line means that this command is going to convert 5 kilos to the appropriate number of pounds.
print "5 kilos =", 5 * kilo, 'pounds'
