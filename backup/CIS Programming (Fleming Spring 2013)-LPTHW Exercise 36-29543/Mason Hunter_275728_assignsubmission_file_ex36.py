#Mason Hunter CIS 120
#Assignment 36
#MAP
#
#
#                                                   - strong-gymnastics
#        -<=70 = ideal sport is jockey or gymnastics
# height-                                           - weak-jockey
#
#
#                                                      -fat-football lineman
#        ->70 = ideal sport is football or basketball                                                       - >= 100 = you can do whatever you want
#                                                      - skinny-hit the weight room----magic strength number
#                                                                                                           - <100 keep training, then pick a sport                                              
#
#
#

def little_sports():
    x = raw_input("Do you consider yourself strong or weak  ")
    if x == "strong":
        print "Try gymnastics"
    elif x == 'weak':
        print "Try jockeying"
    else:
        print "PICK ONE OR THE OTHER"

def big_sports():
    print "Not every tall person can play sports, first we have to know how strong you are."
    print "To do so we have to calculate your strength number"
    bench = input("How much can you bench press")
    squat = input("How much can you squat")
    stnum = (squat - bench) * 2 / 3
    heavy = raw_input("Just an aside, y or n are you fat?")
    if heavy == 'y':
            print "you should be an offensive lineman"
    if heavy == 'n':
        print " your strength number = %d" % stnum
        if stnum > 100:
            print "You are very strong, you can play whatever sport you like"
        elif stnum < 100:
            print "Keep training, then come back later"
        elif stnum == 100: #this is to mess people up
            print "you broke the program"
            list = ['a', 'b', 'c']
            while (len(list)) > 0:
                list.pop()
                list.append("Hello")
print "We are going to determine what sport you should play, enter your height in inches"
height = input("> ")
if height < 70:
    little_sports()
elif height > 70:
    big_sports()
else:
    print "you're too dumb to play sports"