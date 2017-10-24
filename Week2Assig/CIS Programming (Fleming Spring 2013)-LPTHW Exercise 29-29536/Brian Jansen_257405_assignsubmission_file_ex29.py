#Brian Jansen
#Ex 29

#assigns values to variables (people, cats, dogs)
people = 20
cats = 30
dogs = 15

#if people are less than cats then...
if people < cats:
	print "Too many cats!  The world is doomed!"

#if people are greater than cats then...
if people > cats:
	print "Not many cats!  The world is saved!"
	
#If people are less than dogs then...
if people < dogs:
	print "The world is drooled on!"
	
#if people are greater than dogs...
if people > dogs:
	print "The world is dry!"

#Changes the value of dogs
dogs += 5

#if people are greater than or equal to dogs...
if people >= dogs:
	print "People are greater than or equal to dogs."

#if people are less than or equal to dogs...
if people <= dogs:
	print "People are less than or equal to dogs."

#If people are equal to dogs...
if people == dogs:
	print "People are dogs." #And soylent green...is dogs?
	
#1. The if statement is a conditional statment where it basically says if x then y where X can be valuescomparision operators and y is what happens if it returns True.
#2. Since Python is a white space language, the tab acts as the { would in PHP.  Basically as a showing of grouping.
#3. If it's not indented, then it is not part of the if statment and it actually ends it as well.
#4. Yes, you can.
#5. If you change them, then what is outputted is different based on your numbers.
