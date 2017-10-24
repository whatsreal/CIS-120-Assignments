#Marta Sobey
#Assignment number 4. 1/27/2014

#When I print 'cars' the number 100 will appear instead
cars = 100
print "There are", cars, "cars available."
#When I print 'drivers' the number 30 will appear instead
drivers = 30
print "There are only", drivers, "drivers available."
#When I print 'cars' the number 100 will appear instead
cars = 100
#When I print 'drivers' the number 30 will appear instead
drivers = 30
#When I print 'cars_not_driven' the number 70 will appear instead because it is 'cars' (which was assigned the number 100) minus 'drivers' (which was assigned the number 30)
cars_not_driven = cars - drivers
print "There will be", cars_not_driven, "empty cars today."
#When I print 'space_in_a_car' the number 4 will appear instead
space_in_a_car = 4.0
#When I print 'drivers' the number 30 will appear instead
drivers = 30
#When I print 'cars_driven' the number 30 will appear instead because 'cars_driven' signifies 'drivers' which was assigned the value of 30.
cars_driven = drivers
#When I print 'carpool_capacity' the number 120 will appear instead because this signifies 'cars_driven' (which signifies 'drivers' which was assigned the value of 30) multiplied by 'space_in_a_car' (which was assigned the value of 4)
carpool_capacity = cars_driven * space_in_a_car
print "We can transport", carpool_capacity, "people today."
#When I print 'passengers' the number 90 will appear instead
passengers = 90
print "We have", passengers, "to carpool today."
#When I print 'drivers' the number 30 will appear instead
drivers = 30
#When I print 'cars_driven' the number 30 will appear instead because 'cars_driven' signifies 'drivers' which was assigned the value of 30.
cars_driven = drivers
#When I print 'passengers' the number 90 will appear instead
passengers = 90
#When I print 'average_passengers_per_car' the number 3 will appear instead because 'average_passengers_per_car' signifies 'passengers' (which was assigned the value of 90) divided by 'cars_driven' (which signifies 'drivers' which was assigned the value of 30).
average_passengers_per_car = passengers / cars_driven
print "We need to put about", average_passengers_per_car, "in each car."

#This error is saying that 'car_pool_capacity' was not assigned a variable that python can understand. In my line 15 I used 'car_pool_capacity', so I defined each variable that that variable entailed in the three lines above (lines 12 - 15). This helped python follow my command more accurately.
#The 4.0 was not necessary. We would have gotten the same results if we had simply used 4
#A floating point number is a number that includes a decimal point. For example, 4.0 is a floating point number, but 4 is not a floating point number.

print "my calculations"
x = 5
y = 6
print x + y
