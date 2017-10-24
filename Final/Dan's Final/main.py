import re
from deck import *
from player import *
from computerplayer import *
from pokerdecisions import *

plName = raw_input("Please enter your name:")


numAI = input("Please enter the number of computer players:")


while True:
    #Creating each round because this is proof of concept
    #would do something else for final project.
    gamepl = player(plName)
    aiPlayers = []
    for i in range(int(numAI)):
        aiPlayers.append(computerPlayer())

    ourDeck = deck()
    ourDeck.shuffle()


    for i in range(5):
        gamepl.addCard(ourDeck.deal())
        for i in aiPlayers:
            i.addCard(ourDeck.deal())

    gamepl.sortHand()
    for i in aiPlayers:
        i.sortHand()

    check = True
    while check:

        if len(gamepl.hand) == 0:
            check = False
            break
        print "\n\nYour hand is :"
        for i in gamepl.hand:
            print "\t", i.outputCard(), "\n"
        print "Pick a card to remove (1-%d) or press enter to finish:" % (len(gamepl.hand))
        ctr = raw_input("> ")
        ctrchk = re.search(r"[0-9]", ctr)
        if ctr == "":
            check = False
        elif ctrchk is not None and int(ctr) <= len(gamepl.hand) and int(ctr) > 0:
            gamepl.removeCard(int(ctr)-1)
        else:
            print "\n\nThat is not an option"
    while len(gamepl.hand) < 5:
        gamepl.addCard(ourDeck.deal())

    for i in aiPlayers:
        i.keepOrDraw()
        while len(i.hand) < 5:
            i.addCard(ourDeck.deal())

    print "\n\nYour Hand is:"
    for i in gamepl.hand:
        print "\t", i.outputCard(), "\n"

    fok = raw_input("If you want to fold type \'Fold\'> ")
    if fok == "Fold":
        gamepl.hand = []


    for i in range(len(aiPlayers)):
        if aiPlayers[i].foldorCont():
            del aiPlayers[i]

    comparator = []
    if len(gamepl.hand) > 0:
        temp = handRankings[handDecision(gamepl.hand)]
        comparator.append([-1, temp])


    for i in range(len(aiPlayers)):
        temp = handRankings[handDecision(aiPlayers[i].hand)]
        if temp > comparator[0][1]:
            comparator = []
            comparator.append([i, temp])

    if len(comparator) == 1:
        if comparator [0][0] == -1:
            print "\n\nYOU WON!!!!!"
        else:
            print "\n\n%s WON!!!!!" % (aiPlayers[comparator[0][0]].name)
