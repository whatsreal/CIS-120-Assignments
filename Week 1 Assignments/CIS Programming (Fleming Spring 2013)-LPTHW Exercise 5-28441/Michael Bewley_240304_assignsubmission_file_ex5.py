my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print "lets talk about %s" % my_name
print "he's %d inches tall" % my_height
print "hes %d pounds heavy" % my_weight 
print "actually thats not to heavy"
print "hes got %s eyes and %s hair" % (my_eyes, my_hair)
print "his teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "if i add %d, %d, and %d i get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)