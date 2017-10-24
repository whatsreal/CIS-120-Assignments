# Justin Small 1/24/2014

# this line enstantiates variable "cars" as 100 
x = 100
# this line enstantiates variable "space_in_a_car" as 4 
y = 4
# this line enstantiates variable "drivers" as 30
z = 30
# this line enstantiates variable "passengers" as 90
w = 90
# this line enstantiates variable cars_not_driven to the quantity cars minus the quantity drivers
i = x - z
# this line enstantiates variable cars_driven to drivers
j = z
# this line enstantiates variable carpool_capacity to the quantity cars_driven times the quantity space_in_a_car
k = j * y
# this line enstantietes variable average_passengers_per_car to the quantities passengers divided by cars_driven
m = w / j

# this line prints the words "There are", then the quantity "cars", then the words "cars available"
print "There are", x, "cars available."
# this line prints the words "There are only", then the quantity "drivers", then the words "drivers available"
print "There are only", z, "drivers available."
# this line prints the words "There will be" then the quantity "cars_not_driven" then the words "empty cars today."
print "There will be", i, "empty cars today."
# this line prints the words "We can transport", then the quantity "carpool_capacity", then the words "people today."
print "We can transport", k, "people today."
# this line prints the words "We have", then the quantity "passengers", then the words "to carpool today."
print "We have", w, "to carpool today."
# this line prints the words "We need to put about", then the quantity "average_passengers_per_car", then the words "in each car."
print "We need to put about", m, "in each car."