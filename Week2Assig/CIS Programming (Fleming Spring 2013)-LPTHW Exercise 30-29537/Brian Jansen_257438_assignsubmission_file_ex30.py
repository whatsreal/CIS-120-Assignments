#Brian Jansen
#Ex 30

#Define the variables
people = 300
cars = 40
buses = 150
#If cars are greater than people
if cars > people:
	print "We should take the cars."
#else if cars are less than people
elif cars < people:
	print "We should not take the cars."
#if all else fails....
else:
	print "We can't decide."
#If buses are greater than cars and the number of people is greater than or equal to 1	
if buses > cars and people >= 1:
	print "That's too many buses."
#if buses are less than cars and people, more than 0
elif buses < cars and people > 0:
	print "Maybe we could take the buses."
#ELSE OH GEE, ELSE
else:
	print "We still can't decide."
	#If people are greater than buses...we'll just take them.  Doesn't matter if there is a billion people, we're still taking the 150 buses.  But if there's less people than buses.  We give up
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
#elif stands for 'else if' and it provides an alternative 'if' statement if the first one happens to come back false. 
#else is what happens when all the 'if' statements come back as false.

