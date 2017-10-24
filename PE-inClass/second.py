""" Problems:
	1. adding the numbers all up
	2. singling out the last 10 digits
	3. printing them
	4. Find the exponents. """
	
#our range is 1-1000
result = 0
for i in range(1, 1000):
	result += i**i
	
print result % (10**10)