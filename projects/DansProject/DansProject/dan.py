class Person(object):
    
    def __init__(self):
        self.name = None
        self.car = None
        
    def setName(self, name):
        self.name = name
    
    def setCar(self, car):
        self.car = car 
    
    def setWork(self, work):
        self.work = work   
        
    def setSpouse(self, spouse):
        self.spouse = spouse
        
class Employee(Person):

    def __init__(self):
        pass
        
    def setCar(self, car, passengers = 4):
        self.car = car
        self.carpassengers = passengers
        
    def setWork(self, work, salary):
        self.salary = salary
        super(Employee, self).setWork(work)
    

class Animal(object):
    pass

class Pet(Animal):

    def __init__(self, owner):
        self.owner = owner

Abby = Person()
Abby.setName("Abby")
Abby.setWork("Awesomest wife and mother ever")
#Next line won't work because Abby is a Person() not an Employee()
#Abby.setWork("Awesomest wife and mother ever", 1)

Dan = Employee()

Dan.setName("Dan")
Dan.setCar("Matrix", 4)
Dan.setWork("Trinity", 3)

Dan.setSpouse(Abby)
Abby.setSpouse(Dan)
Zinfandel = Pet(Dan)
Zinfandel.owner.name