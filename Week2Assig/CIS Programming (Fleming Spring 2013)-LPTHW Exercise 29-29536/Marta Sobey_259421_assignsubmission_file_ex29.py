#Marta Sobey
#Assignment Number 29. 2/10/14

#Assigns variables values
people = 20
cats = 30
dogs = 15

#These are equality statements with outputs based on their validity
if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "the world is dry!"
	
#add five to the previous value of dogs (15)
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."
	
if people != dogs:
	print "People aren't dogs."	
#The if statement is either going to tell the code to print or not to print based on if the statement is true or not
#it needs to be indented so the code knows that it is going to print based on if the if statement is true or not
#if it isn't indented and indention error appears
#Changing the initial values could change whether the inequalities are true or not and therefore change the ouputs given.