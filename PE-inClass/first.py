from math import sqrt
"""Programming Challenges:
	1. Finding Prime Numbers
		a. divide by a set of numbers: from 2 to itself - 1
	2. Rotating the numbers
		a. convert to string
		b. break the string up into len(num) strings
		c. move characters
		d. convert back to integer
	3. set Range -- limits
	4. List all the circular primes found
		a. When CP found add to list
	5. Length of the list -- # of circular primes """
	
def isPrime(numToCheck):
	"""Accepts an integer to check and see if it is prime.
		by checking the int % x where x is in range 2-(int-1).
		Returns True/False """
	for i in range(2, int(sqrt(numToCheck))):
		if numToCheck % i == 0:
			return False
	return True
		
def rotateNum(num1):
	"""Accepts a number, run a check on all rotations of that number
		to see if they are prime by calling isPrime() on all them.
		Return a list with circular prime numbers.
		If not return False. """
	strNum = str(num1)
	listNums = []
	
	while int(strNum) not in listNums:
		listNums.append(int(strNum))
		tempStr = strNum[1:] + strNum[0]

		if not isPrime(int(tempStr)):
			return False
		strNum = tempStr
	return listNums
	
myList = []
for i in range(1, 100, 2):	

	if isPrime(i):
		tempNum = rotateNum(i)
		if tempNum != False:
			myList.append(tempNum[:])
			
			
print myList
print len(myList)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		