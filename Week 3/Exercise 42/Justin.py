# Justin Small, Exercise 42, 2/16/2014

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name. hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## super Employee has a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a Cat who has-a name satan
mary.pet = satan

## frank is-a Employee who has-a name Frank and has-a Salary 120000
frank = Employee("Frank", 120000)

## frank has-a Dog who has-a name rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut 
harry = Halibut()


#Study Drills:
#1. the object class was added so that there would be a base class from which to derive class
#2. No. Class is a preset word that cannot be used as an object
#3. If I only had the time...
#4. Umm... yeah
#5. I think I get this concept
#6. Yes I will avoid this. 
