#Definitions for text-based adventure game
#To be used in CIS 120 February 10, 2014
#Prof. Dan Fleming

from sys import exit

class Obst(object):

    def __init__(self, obst):
        self.name = obst[0]
        self.solution = obst[1]
        self.solutionText = obst[2]
        
    def Give(self, item):
        if (item == self.solution):
            print self.solutionText
            if (self.solutionText == "You Win!"):
                print "Good Job!"
                exit(0)
            return 0
        else:
            print "You died! Goodbye"
            exit(0)
            

class Room(object):
    
    def __init__(self, name, obst = None, item = None):
        self.roomname = name
        self.adjrooms = {}
        if (obst != None):
            self.obstacle = Obst(obst)
        else:
            self.obstacle = None
        self.inRoom = item
        
        
    def Info(self):
        toprint = "You are in " + self.roomname + ".\n"
        for key, value in self.adjrooms.iteritems():
            toprint += key + " is a room.\n"
        if(self.inRoom != None):
            toprint += "In this room there is a " + self.inRoom + "."
        if(self.obstacle != None):
            toprint += "There is a " + self.obstacle.name + " blocking your way."
        return toprint
    
    def PopulateAdjoining(self, adjoiningrooms):
        """Takes a list of adjoining rooms and creates them so the player can move.
        Expect a dict of type direction : room """
        for key, value in adjoiningrooms.iteritems():
            self.adjrooms[key] = value
            
    def MoveRoom(self, direction):
        """Move rooms if possible."""
        if (self.obstacle != None):
            print "You still need to defeat %s before you can move!" % self.obstacle.name
            return None
        elif (direction in self.adjrooms):
            return self.adjrooms[direction]
        else:
            print "There is no room in that direction."
            
            
    def GetItem(self, item):
        if(item == self.inRoom):
            inRoom = None
            return item
        else:
            print "That item isn't in this room."
            return None            
                
                
                
                
                
class Player(object):

    def __init__(self, playername):
        """Initialize the player. Require a name that we will use.
        Also initializes the player's inventory as an empty list"""
        self.name = playername
        self.inventory = []
        self.CurrentRoom = Room('...')
        
    def CheckInventory(self, item):
        for i in self.inventory:
            if (i == item):
                return 0
        return 1
    
    def TakeAction(self, act):
        """Basic action taking.  Expect a string."""
        lActions = act.split(' ')
        if (lActions[0] == 'give'):
            self.GiveItem(lActions[1])
        elif (lActions[0] == 'go'):
            movement = self.CurrentRoom.MoveRoom(lActions[1])
            if (movement != None):
                self.CurrentRoom = movement
            print self.CurrentRoom.Info()
        elif(lActions[0] == 'get'):
            item = self.CurrentRoom.GetItem(lActions[1])
            if (item != None):
                self.inventory.append(item)
                print "The %s is in your inventory." % item
                self.CurrentRoom.inRoom = None
            else:
                print "I could not get that item."
        elif(lActions[0] == 'look'):
            print self.CurrentRoom.Info()
        else:
            print "I don't understand what you want to do."
            
    def GiveItem(self, item):
        if (self.CurrentRoom.obstacle != None):
            given = self.CurrentRoom.obstacle.Give(item)
            if (given == 0):
                self.RemoveItem(item)
                self.CurrentRoom.obstacle = None
        
        
    def RemoveItem(self, item):
        mylist = []
        for i in self.inventory:
            if(i != item):
                mylist.append(i)
        self.inventory = mylist
        

        