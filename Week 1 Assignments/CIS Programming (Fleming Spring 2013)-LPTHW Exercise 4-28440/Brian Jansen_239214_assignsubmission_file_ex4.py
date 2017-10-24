#Brian Jansen
#Ex 4

#The below lines make the variables and then dictate what the variables are or mean.  (X = Y) Where X is the variable name and Y is the value.  Some of the lines below work with math as well within the value.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#The lines below print out sentences where the variable is expressed within the sentence. 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#In the error he mentions in the study drills, he used the name "car_pool_capacity" rather than "carpool_capacity." What a dummy, am I right?
#Removing the .0 from the variable just removes the decimal point and extra number from math equations that use that particular variable.
