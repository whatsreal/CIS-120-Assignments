#Marta Sobey 
#Assignment Number 42. 2/17/14

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

#dog is-a animal
class Dog(Animal):
	#self has-a name
    def __init__(self, name):
        
        self.name = name

#class cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## self has-a name
        self.name = name

## class person is-a object
class Person(object):

    def __init__(self, name):
        ## self has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## start with employee which is inheriting the person which is then being passed a name
        super(Employee, self).__init__(name)
        ## self has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has-a pet named satan
mary.pet = satan

## Frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

#object class is a base class that everything inherits from
#yes you could not use a class like it is an object. objects are concrete but classes are abstract
#the diamond problem is known with multiple inheritance
#lists make for longer has-a or is-a statements. ex) Marta has many clothes
#we talked about has-many relationships in person
#is-many relationships can happen. Don't do it!
