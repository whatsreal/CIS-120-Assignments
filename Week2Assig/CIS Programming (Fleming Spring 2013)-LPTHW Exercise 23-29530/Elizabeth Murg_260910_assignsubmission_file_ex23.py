#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/"""
#This tells the computer what plan to use.
import os

#not sure what a class is. but dog(object) is probably an argument of class
class Dog(object):
	#these next lines define a function 
    def __init__(self):
		#and self.name will assign a variable "dog" to self.name
        self.name = "Dog"
#line 16 will define a new function called bark which has the argument (self)
    def bark(self):
	#it will return the string "woof!"
        return "woof!"


class Cat(object):
	#line 23 defines a new function called __init__ with the argument (self)
    def __init__(self):
		#a variable self.name is assigned "cat"
        self.name = "Cat"
#a new function meow is defined with the argument (self) which will return "meow!"
    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):
#a new function __init__ is defined with the argument (self)
    def __init__(self):
		#a new variable is assigned "car"
        self.name = "Car"
# a new function make_noise is defined with two arguments (self, octane_level)
    def make_noise(self, octane_level):
		#it will return the string "vroom" with a different way of printing
        return "vroom{0}".format("!" * octane_level)


class Adapter(object):
#this is just a really long comment 
    """
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