#Marta Sobey
#Assignment Number 23. 2/10/14

#importing the whole os package
import os

#I don't know what class is
class Dog(object):
    def __init__(self): #defining functions. pink is function. black is argument
        self.name = "Dog" #assigning a variable

    def bark(self): #defining a function
        return "woof!" #returning a string "woof!"


class Cat(object):
    def __init__(self): #same as line 9
        self.name = "Cat" #same as line 10

    def meow(self): #same as line 9
        return "meow!" #same as line 10


class Human(object):
    def __init__(self): #same as line 9
        self.name = "Human" #same as line 10

    def speak(self): #same as line 9
        return "'hello'" #same as line 10


class Car(object):
    def __init__(self): #same as line 9
        self.name = "Car" #same as line 10

    def make_noise(self, octane_level): #defining a function with two arguments
        return "vroom{0}".format("!" * octane_level) #.format is a different way to print


class Adapter(object):
    """ #a big comment
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))

    >>> objects = []
    >>> dog = Dog()
    >>> objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    >>> cat = Cat()
    >>> objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    >>> human = Human()
    >>> objects.append(Adapter(human, dict(make_noise=human.speak)))
    >>> car = Car()
    >>> car_noise = lambda: car.make_noise(3)
    >>> objects.append(Adapter(car, dict(make_noise=car_noise)))

    >>> for obj in objects:
    ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """