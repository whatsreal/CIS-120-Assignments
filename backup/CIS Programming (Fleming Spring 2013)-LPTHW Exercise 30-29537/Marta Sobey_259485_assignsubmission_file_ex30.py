#Marta Sobey
#Assignment Number 30. 2/10/14

#Assigns variables to different values
people = 10
cars = 50
buses = 75

# These are all equality statements. If this statement is true, the first print statement will be printed.
if cars > people:
	print "We should take the cars."
#If the first statement is false but this statement is true, this next print statement will be printed.
elif cars < people:
	print "We should not take the cars."
#If the other two statements are false, this final print statement will be printed.
else:
	print "We can't decide."
# These are all equality statements. If this statement is true, the first print statement will be printed.
if buses > cars:
	print "That's too many buses."
#If the first statement is false but this statement is true, this next print statement will be printed.
elif buses < cars:
	print "Maybe we could take the buses."
#If the other two statements are false, this final print statement will be printed.
else:
	print "We still can't decide."
# These are all equality statements. If this statement is true, the first print statement will be printed.	
if people > buses:
	print "Alright, let's just take the buses."
#If the first statement is false but this statement is true, this next print statement will be printed.
else:
	print "Fine, let's stay home then."
# These are all equality statements. If this statement is true, the first print statement will be printed.	
if cars > people and buses < cars:
	print "OK"
#If the first statement is false but this statement is true, this next print statement will be printed.
else:
	print "Bad"
	
#elif and else are like saying either or. If the statement is true, print what is under 'if'. If it is not true, print what is under 'elif'.