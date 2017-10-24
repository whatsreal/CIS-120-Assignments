# Justin Small, Excersise 21, 2/9/2014

def add(a, b):
    print "ADDING %d + %d" % (a, b)
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
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(weight, add(iq, multiply(weight, divide(age, 32))))

print "That becomes: ", what, "Can you do it by hand?"

where = subtract(iq, multiply(weight, divide(2, add(height, divide(iq, 2)))))

print "That becomes: ", where

#Study Drills
#1. I'm pretty sure I know what return does.
#2. 35+(74-(180*(50/2))) is the formula
#3. Did it and my result was 410
#4. Did it. I think this is what you were looking for. 50-(180*(2/(74+(50/2)))))q
