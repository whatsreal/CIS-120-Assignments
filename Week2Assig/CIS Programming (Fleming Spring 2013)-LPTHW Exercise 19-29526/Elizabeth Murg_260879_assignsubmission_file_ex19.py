#Elizabeth Murg
#Assignment Number 19. 2/7/2014.

#This first block will define the function and give variables and say what should print out when the programs calls for the function
def cheese_and_crackers (cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

#This block will print out a line and then using the function will plug in the numbers into the format characters in the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#This block will print line 16 and then plug in the variables into the format characters of the function
print "OR, we  can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#This line just changes the name of the arguments for the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#This block will perform operations and then use the answers to plug into the format characters in the statement
print "We can even do math inside too:"
cheese_and_crackers (10 + 20, 5 + 6)

#This will perform another operation adding to the arguments previously defined and once again plug them into the format characters
print "And we can combine the two, variables and math:"
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers+1000)
