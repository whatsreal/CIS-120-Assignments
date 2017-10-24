##################################
#
#
#Midterms Problems
#
#
###############################

""" Variables are all objects."""
x = 1 #Object of type int()
x = int(1) #More explicitly
y = "A String"
y = str("A String")
z = 1.2 #Float
w = list([1,2])
#Those are all built-in but we can do our own:

#The Call:
a = MyClass()

#MyClass is not defined by Python, we need to define it.
class MyClass(Object):
    """Let's make a class!"""
    def __init__():
        """Our Initializer, it doesn't have to do anything
           but it can if we want it to."""
        #Lets add a list, just for fun.
        myList = ["Dan", "Abby", "Anna", "Kenneth", "Toasty", ""]

    #Functions inside a class should not interact with the user
    #Except by passing in arguments

    def __search(self, searchTerm):
        """Search through our list and return the position of
           the matching element."""
        for i in range(len(self.myList)):
            if self.myList[i] == searchTerm:
                return i
        return Null

    #Why return that?
    #Code-reuse.

    def search(self, searchTerm):
        """This is the version of search that the user will use."""
        pos == self.__search(searchTerm)
        if pos is not Null:
            #Print the stuff here...
            return
        else:
            print "We could not find that record."

    def add(self, itemToAdd):
        """Add an item to the list, lets make sure no dups."""
        if self.__search(itemToAdd) != Null:
            self.myList.append(itemToAdd)

    #Notice we were able to use __search() twice, we didn't have to recode
    #The same functionality into two separate functions.





################################
#
#
#Big O Notation Examples
#
#
################################

#O(1)
def StringLength(s):
    """Return the length of any string"""
    if len(s) > 0:
        return len(s)
    else:
        return Null

#O(n)
def PrintSingle(s):
    """Print a string one character at a time"""
    for i in s:
        print i


#O(log(n))
#Binary Search
#We'll learn about it next week.
def BinarySearch(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m


#O(n**2)
def DuplicateChars(myString):
    """Check to see if there are any duplicate characters in myString
       Why? Because I can."""
    for i in range(len(myString)):
        for j in range(len(myString)):
            if i == j: #Don't compare a character to itself
                continue
            if myString[i] == myString[j]:
                return True
    return False

#O(2**n)
#If you're writing a function that takes this kind of time...
#You are in big big trouble anyway.
