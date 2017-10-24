from textadv import *

#Define the various obstacles as lists of items.

hungryDog = ['Hungry Dog', 'meat', 'The hungry dog goes off to the corner to eat his food.']
kid = ['Your Son', 'crayon', 'Your son goes off to draw on the walls with the crayon.']
table = ['Table', 'bowl', 'You Win!']


#Define the various rooms. Include obstacles.
foyerRoom = Room('Foyer', None, 'crayon')
livingRoom = Room('Living Room', kid, 'bowl')
diningRoom = Room('Dining Room', hungryDog)
kitchenRoom = Room('Kitchen', table)
libraryRoom = Room('Library', None, 'meat')

#Lay out the map of rooms.

foyerRoom.PopulateAdjoining(dict([('north', livingRoom)]))
livingRoom.PopulateAdjoining(dict([('south', foyerRoom), ('east', libraryRoom), ('west', diningRoom)]))
libraryRoom.PopulateAdjoining(dict([('west', livingRoom)]))
diningRoom.PopulateAdjoining(dict([('east', livingRoom), ('north', kitchenRoom)]))
kitchenRoom.PopulateAdjoining(dict([('south', diningRoom)]))

#Instantiate the player.

pName = raw_input("What is your name? ")
myPlayer= Player(pName)
myPlayer.CurrentRoom = foyerRoom

print myPlayer.CurrentRoom.Info()
#Start the game!


while(True):
    print "What do you want to do?"
    myPlayer.TakeAction(raw_input("> "))