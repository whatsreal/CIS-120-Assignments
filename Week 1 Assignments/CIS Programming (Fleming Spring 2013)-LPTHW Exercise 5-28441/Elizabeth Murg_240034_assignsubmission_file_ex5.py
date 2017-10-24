#Elizabeth Murg
#Assignment Number 5. 1/27/14
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight) 

name2 = 'Betty'
age2 = 18 # years old

#%s prints what is within the quotations of the string variable, while %r includes everything.
print "Let's now talk about %s." % name2
print "Let's now talk about %r." % name2

#For number variables, %r and %d don't seem to make a difference. 
print "She is %d years old." % age2
print "She is %r years old." % age2

#First, I assign a variable for the conversion of inches to centimetres
inch = 2.54 # (centimetres) 
#Then using strings and the variable, I make a problem and see if it works.
print "I have 7 inches of wood which is about", 7 * inch, "centimetres." 
print 7 * 2.54 
#It works :) 

#Again, I assign a variable for the conversion of pounds to kilos.
pound = 0.453952 # (kilograms)
#Then using strings and variables, I check if it works.
print "I have 13 pounds of sugar which is approximately", 13 * 0.453952, "kilograms." 
print 13 * 0.453952
#It works.





