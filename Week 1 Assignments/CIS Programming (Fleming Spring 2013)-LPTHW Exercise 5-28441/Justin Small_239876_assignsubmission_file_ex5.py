name = 'Zed A. Shaw'
age = 35 # not a lie
height = round (74 * 2.54) # centimeters 
weight = round (180 * 0.453) # kilos
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r centimeters tall." % height
print "He's %r kilos heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)