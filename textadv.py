#Definitions for text-based adventure game
#To be used in CIS 120 February 10, 2014
#Prof. Dan Fleming

from sys import exit

class Obst(object):

    def __init__(self):
        """we need to initiate the obstacle with a name, solution and solution text
        the solution will be what fixes this obstacle.  Solution text is what we print. """
        
    def Give(self, item):
        """We need to give the item to the obstacle.
        Check to see if this item is the solution to our obstacle.
        If it is print the solution text and check to see if the player won.
        Otherwise print a message telling the player they died and quit."""
            

class Room(object):
    
    def __init__(self, name, obst = None, item = None):
        """Create the room with a name, an obstacle, and an item (optional)"""
        
        
    def Info(self):
        """Print all the information about the room.
        Include what rooms adjoin, 
        any obstacles in the room,
        and any items in the room."""
    
    def PopulateAdjoining(self, adjoiningrooms):
        """Takes a list of adjoining rooms and creates them so the player can move.
        Expect a dict of type direction : room """
        
            
    def MoveRoom(self, direction):
        """Move rooms if possible.  Check to see if there is a room in the direction
        also check to see if the obstacle has been vanquished.  
        If it is possible to move in the direction then return the room that is in that direction"""
        
            
            
    def GetItem(self, item):
        """Check to see if the item requested is in the room.
        If it is return the item.  If not return None."""
                
                
                
                
class Player(object):

    def __init__(self, playername):
        """Initialize the player. Require a name that we will use.
        Also initializes the player's inventory as an empty list
        Also initialize a Current Room."""
        
        
    def CheckInventory(self, item):
        """Check the player's inventory for a particular item.
        Return 0 if they have it 1 if they don't."""
    
    def TakeAction(self, act):
        """Basic action taking.  Expect a string.
        Split the string on spaces as we're expecting more than one word.
        Actions we need to account for are 'give' 'go' 'get' and 'look'
        pass to the appropriate function.
        Make sure you have an else for random text inputs."""
            
    def GiveItem(self, item):
        """make sure there is an obstacle in the room.  
        Make sure that you have that item in your inventory.
        Try giving the item to the obstacle.
        Make sure to remove the obstacle (and the item from your inventory)
        if the giving is successful."""
        
    def RemoveItem(self, item):
        """loop over the self.inventory and use it to create a new list
        that includes all the current items except the one you want to delete."""
        

        