#Brian Jansen
#Ex 19

#The following makes a function based on two variables
def cheeseandcrackers(cheesecount, crackerboxes):
	print "You have %d cheeses!" % cheesecount
	print "You have %d boxes of crackers!" % crackerboxes
	print "Man, that's enough for a party! \nGet a blanket.\n"
	
#The following executes the fuction with two defined numbers
print "We can give the function numbers directly:"
cheeseandcrackers(20,30)

#These lines creates two variables, then uses them to execute the function.
print "OR, we can use variables"
cheeseamount = 10
crackeramount = 10
cheeseandcrackers(cheeseamount,crackeramount)

#These lines prints, then calls the function with math
print "We can math in it too!"
cheeseandcrackers(10+20,5+6)

#math and variables....
print "And we can do both!"
cheeseandcrackers(cheeseamount+5,crackeramount+6)

#Study Drills
def inchestocentimeters(inches):
	centimeters = inches*2.54
	print "%r inch is equal to %r centimeters\n" % (inches,centimeters)
	
inchestocentimeters(1)
inchestocentimeters(2)
inchestocentimeters(3)
inchestocentimeters(4)
inchestocentimeters(5)
inchestocentimeters(6)
inchestocentimeters(7)
inchestocentimeters(8)
inchestocentimeters(9)
inchestocentimeters(10)
