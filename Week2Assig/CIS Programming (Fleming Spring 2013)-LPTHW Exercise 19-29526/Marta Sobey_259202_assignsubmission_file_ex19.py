#Marta Sobey
#Assignment Number 19. 2/10/14

#This line defines strings in terms of the two variables inside the parentheses. The other lines simply print what is inside quotes replacing the %d characters with the content from the respective variables.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# This line prints what is inside quotes followed by the content that was defined to 'cheese_and_crackers' while replacing the %d characters with the numbers 20 and 30.
print "We can just give the function numbers directly:" 
cheese_and_crackers(20, 30)
# This line prints what is inside quotes followed by the content that was defined to 'amount_of_cheese' and 'amount_of_crackers' while replacing the %d characters with the numbers 10 and 50.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#defines 'cheese_and_crackers' with the different variables 'amoutn_of_cheese' and 'amount_of_crackers'
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#print what is inside quotes while changing the %r characters with the addition of 10 and 20 then 5 and 6
print "We can even do math inside too:" 
cheese_and_crackers(10 + 20, 5 + 6)
#prints what is inside quotes while replacing the %r characters with the addition of the value of 'amount_of_cheese' and 100 and the addition of the value of the 'amount_of_crackers' and 1000.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#All the comments from above are going to be the same because I used the same template.
def markers_and_crayons(markers_count, boxes_of_crayons):
	print "You have %d markers!" % markers_count
	print "You have %d boxes of crayons!" % boxes_of_crayons
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:" 
markers_and_crayons(20, 30)

print "OR, we can use variables from our script:"
amount_of_markers = 10
amount_of_crayons = 50

markers_and_crayons(amount_of_markers, amount_of_crayons)

print "We can even do math inside too:" 
markers_and_crayons(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
markers_and_crayons(amount_of_markers + 100, amount_of_crayons + 1000)

# You can run the function different ways by giving it different numbers, variables, and making into math problems.
