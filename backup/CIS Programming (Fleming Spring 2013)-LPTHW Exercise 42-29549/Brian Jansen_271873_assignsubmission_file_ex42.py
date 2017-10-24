#Brian Jansen
#Ex 42
#Copy-pasted this one since it was more about the comments than the code....

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is an animal
class Dog(Animal):

    def __init__(self, name):
        ## The object "dog" has a name"
        self.name = name

## Cat is an animal
class Cat(Animal):

    def __init__(self, name):
        ## object "cat" also has a name
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## "person" has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name) #This causes this class to inherit the INIT function of the parent....?
        ## employees have a salary
        self.salary = salary

## fish is an object
class Fish(object):
    pass

## salmon is a fish
class Salmon(Fish):
    pass

## halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## satan is mary's pet
mary.pet = satan

## frank is an employee and has a 120000 salary
frank = Employee("Frank", 120000)

## Rover is frank's pet
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
