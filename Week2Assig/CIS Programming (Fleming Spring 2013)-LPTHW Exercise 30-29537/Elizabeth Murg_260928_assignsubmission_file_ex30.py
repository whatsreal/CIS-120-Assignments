#Elizabeth Murg
#Assignment Number 30. 2/10/2014.

people = 50
cars = 50 
buses = 50

#each of these blocks gives three options based on the variables defined above. If one of the variables is greater than the other it will print something if the other variable is greater it will print something else.
#otherwise, like if they're equal, it will print something else. This is for each of the blocks below. 
if cars> people:
	print "We should take the cars."
elif cars < people: 
	print "We should not take the cars."
else: 
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else: 
	print "Fine let's stay home then."
	
#i changed them to all be equal and we ended up staying home. because no one could decide. each block printed the else statemetn (the last option)