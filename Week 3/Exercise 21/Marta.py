#Marta Sobey
#Assignment Number 21. 2/10/14

def add(a, b):
	print "ADDING %d + %d" %(a, b)
	return a + b

def subtract(a, b):
		print "SUBTRACTING %d - %d" % (a, b)
		return a - b
		
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100 ,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#I am going to perform the actual math. 
# x = (iq (100/2 = 50))/2 = 25
# multiply = (weight (90*2 = 180))*(x (25)) = 4500
# subtract = (height (78-4 = 74)) - (multiply (4500)) = -4426
# add = (age (30+5 = 35)) + (subtract (-4426)) = -4391

what = add(age, multiply(height, multiply(weight, subtract(iq, 2))))
#I am going to perform the actual math. 
# x = (iq (100/2 = 50)) - 2 = 48
# multiply = (weight (90*2 = 180))*(x (48)) = 8640
# multiply = (height (78-4 = 74)) * (multiply (8640)) = 639360
# subtract = (age (30+5 = 35)) + (subtract (639360)) = 639395

print "That becomes: ", what, "Can you do it by hand?"

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
number = divide(500, 5)

# f = ma. multiply (mass, acceleration)
