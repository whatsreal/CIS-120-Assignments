#Elizabeth Murg
#Assignment Number 4. 1/27/14

#This variable will tell us how many cars are available.
cars = 100
#This variable will tell us how many seats are available in each car.
space_in_a_car = 4.0
#This variable will tell us how many drivers are available.
drivers = 30
#This variable will tell us how many passengers there are.
passengers = 90
#This variable will let us know how many cars will not be used by subtracting the number of drivers from the number of cars.
cars_not_driven = cars - drivers
#This variable will equal the number of drivers to the number of cars being driven.
cars_driven = drivers
#This variable will show how much available space there is for the passengers.
carpool_capacity = cars_driven * space_in_a_car
#This variable will show how many people will be in each car.
average_passengers_per_car = passengers / cars_driven

#This line will print exactly what is in quotations and then exchange the variable out of quotations for the number of cars. 
print "There are", cars, "cars available."
#This line will print exactly what is in quotations and then exchange the variable out of quotations for the number of drivers available.
print "There are only", drivers, "drivers available."
#This line will print exactly what is in quotations and then exchange the variable out of quotations for the number of cars that will not be used.
print "There will be", cars_not_driven, "empty cars today."
#This line will print exactly what is in quotations and then exchange the variable out of quotations for the number of people that can go in the cars.
print "We can transport", carpool_capacity, "people today."
#This line will print exactly what is in quotations and then exchange the variable out of quotations for the number of passengers.
print "We have", passengers, "to carpool today."
#This line will print exactly what is in quotations and then exchange the variable out of quotations for the average amount of passengers that each car will have. 
print "We need to put about", average_passengers_per_car, "in each car."

#The error is the he wrote car_pool_capacity when originally he had named the variable carpool_capacity. 
#He was asking for a variable that did not exist.
#Using 4.0 for space_in_a_car is not necessary because the number anyway is 120.0 and you don't need that last zero. In fact, it is probably better not to use it here because you can't fraction people. 
#A floating point number is a number that has the decimal representation as well not just the integer
