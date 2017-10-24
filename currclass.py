myObj = someClass()

def function1(george, ralph, aSomeClassObj):
	"""Accepts two numbers and returns 
	   the first ^ second """
	global myObj
	laura = george**ralph #raising george to ralph assigning to laura
	aSomeClassObj.size = laura
	return laura, aSomeClassObj




number, myObj = function1(2, 3, myObj)


class Person(object):

	def __init__(self, myName = ""):
		self.name = myName
		
	
		
		
		
		
x = Person()
y = Person("Dan")
z = Person("George")

print z.name
print x.name
print y.name





mlist = [1,2,3,4,5,6,7]

zlist = []

tempInt = mlist.pop()

zlist.append(tempInt)

zlist.append(mlist.pop)

mlist == [2,3,4,5,6,7]
zlist == [1]
































