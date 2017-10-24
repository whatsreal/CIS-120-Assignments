#Mason Hunter
#Assignment 42
class Animal(object):
    pass #animal isa object
    
class Dog(Animal): #dog isa anmial
    def __init(self, name):
        self.name = name #dog hasa name
        
class Cat(animal): #cat isa animal
    def __init__(self, name)L
        self.name = name #cat hasa name
        
class Person(object): #Person isa object
    def __init__(self, name):
        self.name = name #person hasa name
        
        self.pet = None # person hasa pet
        
class Employee(Person): #an employee isa person
    def __init__(self, name, salary): #employee has a self/name/salary
       super(Employee, self).__init__(name) #super isa employee's name
       self.salary = salary #employee hasa salary

class Fish(object):#fish isa object
    def __init__ (self, color, numoffins)
        self.color= color_of_fish
        self.numoffins = number_of_fins_that_a_fish_has
class Salmon(Fish): #salmon isa fish
    pass
class Halibut(Fish):  #halibut isa fish
    pass

rover = Dog("Rover") #rover isa dog

satan = Cat("Satan") #satan isa cat

mary = Person("mary") #mary isa person

mary.pet = satan #mary has a pet named satan who's a cat

frank = Employee("Frank", 12000) #frank isa employee with a salary of 12000

frank.pet=rover #frank has a pet named rover who's a dog

flipper = Fish()#flippet isa fish

crouse = Salmon() #crouse isa salmon fish

harry = Halibut() #Harry isa halibut fish

#SD 1: I couldn't find any additional history of why python has an object class other than what was in learnpythonthehardway
#SD 2: yes if you stick it in another class
#SD 3: I filled out the fish class to make an init function that makes variables for its color and number of fins.
#SD 6: There probably is that relationship but it's really complicated