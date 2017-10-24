#Michael Bewley

from sys import exit

def food_room():
    print "This room is full of burgers and fries.  How much do you want to eat?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Mmmmmm you're not too hungry!"
        exit(0)
    else:
        dead("Wow! Lay off the fries!")


def prospector_room():
    print "There is an angry prospector here."
    print "The prospector has a sandwich."
    print "The prospector is in front of another door."
    print "How are you going to make him move?"
    prospector_moved = False

    while True:
        next = raw_input("> ")

        if next == "take sandwich":
            dead("The prospector hits you with his shovel.")
        elif next == "give gold" and not prospector_moved:
            print "The prospector has moved from the door. You can now enter."
            bear_moved = True
        elif next == "take gold back" and bear_moved:
            dead("The prospector throws you off the bridge.")
        elif next == "open" and prospector_moved:
            food_room()
        else:
            print "Say what?."


def witch_room():
    print "Here you see the wicked witch of the west."
    print "She staresinto your soul and is about to strike."
    print "Do you flee for your life or call your mother?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "call" in next:
        dead("You are way past your bedtime!")
    else:
        witch_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You walk through a forest and see some doors."
    print "There is a door to your right and left."
    print "Where do you go?"

    next = raw_input("> ")

    if next == "left":
        prospector_room()
    elif next == "right":
        witch_room()
    else:
        dead("You set off a booby trap and die.")


start()
