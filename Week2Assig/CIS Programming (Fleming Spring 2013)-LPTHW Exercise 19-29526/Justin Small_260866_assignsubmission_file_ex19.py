# Justin Small, Excersise 19, 2/9/2014

#this declares function cheese_and_crackers with the arguements "cheese_count, and boxes_of_crackers" 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	  #this line prints a message containing "cheese_count"
    print "You have %d cheeses!" % cheese_count
    #this line prints a message containing "boxes_of_crackers"
    print "You have %d boxes of crackers!" % boxes_of_crackers
    #this line prints a silly message
    print "Man that's enough for a party!"
    #so does this one, but with a new line at the end
    print "Get a blanket.\n"

#this line explains one way to assign arguements to a function
print "We can just give the function numbers directly:"
#this line directly assigns the numbers 20, and 30 to cheese_count and boxes_of_crackers respectively
cheese_and_crackers(20, 30)

#this line explains another way to assign arguements to a function
print "OR, we can use variables from our script:"
#this line sets variable amount_of_cheese equal to 10
amount_of_cheese = 10
#this line sets variable amount_of_crackers equal to 50
amount_of_crackers = 50

#this line assigns variables amount_of_cheese and amount_of_crackers to function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#this line explains yet another way to assign arguements to a function
print "We can even do math inside too:"
#this line directly assigns the arguements 10+20 and 5+6 to the function cheese_and_crackers
cheese_and_crackers(10 + 20, 5 + 6)

#this line declares yet another way to assign arguements to a function
print "And we can combine the two, variables and math:"
#this line assigns the arguements amount_of_cheese + 100 and amount_of_crackers + 1000 to function cheese_and _crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study Drills
#1. Did it
#2. Done and Done
#3. This will take too long
