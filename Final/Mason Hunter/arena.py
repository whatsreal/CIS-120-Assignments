from human_player import *#imports all the relevant functions
from dealer import *
from computer_player import *
from time import sleep
from random import randint
import os
class arena(object):
    def play(self, user, player1, player2, player3, dealer):
        """This function is the "game play", it takes as arguments the players and the dealer and starts the game"""
        zzz = user
        prep = player1
        cowboy = player2
        gent = player3
        Bernie_Mac = dealer
        bet_checker = 0#to make sure the user bets a valid integer which is not zero
        while True:
            your_bet = raw_input("How much you like to bet?(You can only bet whole dollars in integer form (like 5) > ")
            while bet_checker != 9876:
                try:
                    your_bet = int(your_bet)
                    bet_checker = 9876
                    while your_bet == 0:
                        print "You have to bet something"
                        your_bet = raw_input("How much you like to bet?(You can only bet whole dollars in integer form (like 5) > ")
                        your_bet = int(your_bet)
                except ValueError:
                    print "That was not an integer\n"
                    your_bet = raw_input("How much you like to bet?(You can only bet whole dollars in integer form (like 5) > ")
                    bet_checker = 0
                    
            zzz.gamble(your_bet)#reduces the user's winnings in light of their wager
            pot = your_bet + prep.wager + cowboy.wager + gent.wager#creates the pot
            cowboy.gamble(cowboy.wager)#these functions reduce the CPU's winnings after their wager
            gent.gamble(gent.wager)
            prep.gamble(prep.wager)
            os.system('cls')
            zzz.hand = Bernie_Mac.deal()#the user is dealt a hand
            prep.hand = Bernie_Mac.deal()#the CPU's are all dealt a hand
            cowboy.hand = Bernie_Mac.deal()
            gent.hand = Bernie_Mac.deal()
            for i in zzz.hand:#if the User is dealt and ace they decide whether it will be a 1 or a 10
                if i[1] == 99:
                    turtle = 0
                    while turtle != 5 :
                        print "Your hand is: ", zzz.hand
                        try:
                            i[1] = input("Do you want that Ace to be a 1 or a 10? > ")
                            turtle = 5
                        except NameError:
                           print "That was not an integer \n"
                    if i[1] == 1:
                        pass
                    elif i[1]== 10:
                        pass
                    else:#if they try to get fancy and make the ace count as something other than 1 or 10 the user gets kicked out of the casino
                        print "You dirty cheater, get out of here and don't come back!!!"
                        exit()
                            
            os.system('cls')
            print "Your hand is: ",zzz.hand#shows the user their hand
            zzz.hand_score = Bernie_Mac.score(zzz.hand) #computes the user hand score
            prep.hand_score = Bernie_Mac.score(prep.hand)#computes the CPU's hand scores
            cowboy.hand_score = Bernie_Mac.score(cowboy.hand)
            gent.hand_score = Bernie_Mac.score(gent.hand)
            print "Eugene Forrester's hand is: ", prep.hand #shows the user the other player's hands
            print "Rooster Cogburn's hand is: ", cowboy.hand
            print "Lord Havisham's hand is : ", gent.hand

            while prep.hand_score <= prep.threshold:#if his hand score is less than his threshold, he will take a hit, if his score above his threshold he will sit
                print "Eugene is taking a hit"
                card = Bernie_Mac.deal_a_hit()
                prep.hit(card)
                prep.hand_score = Bernie_Mac.score(prep.hand)
            pq = randint(0, len(prep.quips)-1)#picks a random integer within the length of the length of his quips
            print "Eugene is choosing not to take another hit\n"
            if prep.hand_score < 14:
                print "Dealer: C'mon Chicken!\n", "Eugene replies: ", prep.quips[pq], "\n\n\n\n"#if Eugene sat while is score was low, the dealer taunts him and he responds with one of his quips
            cq = randint(0, len(cowboy.quips)-1)        
            while cowboy.hand_score <= cowboy.threshold:#if his hand score is less than his threshold, he will take a hit, if his score above his threshold he will sit
                print "Rooster is choosing to take a hit"
                if cowboy.hand_score > 15:
                    print "Dealer: Bold Move Cotton!\n", "Rooster Replies: ", cowboy.quips[cq]#if Rooster makes a "risky" hit, the user tells him how bold that was, and Rooster replies
                card = Bernie_Mac.deal_a_hit()
                cowboy.hit(card)
                cowboy.hand_score = Bernie_Mac.score(cowboy.hand)
            if cowboy.hand_score < 22:#as long as rooster hasn't busted and his hand score is above his threshold he will sit
                print "Rooster is choosing not to take another hit\n\n"
            while gent.hand_score <= gent.threshold:#if his hand score is less than his threshold, he will take a hit, if his score above his threshold he will sit
                print "Lord Havisham is choosing to take a hit"
                card = Bernie_Mac.deal_a_hit()
                gent.hit(card)
                gent.hand_score = Bernie_Mac.score(gent.hand)
            if gent.hand_score < 22:
                gq = randint(0, len(gent.quips)-1)#the dealer taunts LH a bit, and he responds
                print "Lord Havisham is choosing not to take another hit\n\nDealer: You won't win if you don't take a risk\n", "Lord Havisham replies: ", gent.quips[gq], "\n\n\n\n"
            while zzz.hand_score < 22:#gives the User the option to hit or sit (as long as they haven't busted) and the while loop and try/except is in case they hit twice or put in a something other than 1 of 2
                try:                
                    pc = input("Your move.  Type '1' if you want to hit, or '2' if you want to sit. > ")
                    if pc == 1:
                        card = Bernie_Mac.deal_a_hit()
                        card = zzz.score(card)
                        if card == False:#if they try to get tricky with an ace, the human user score function outputs false and the user gets kicked out of the casino
                            exit()
                        zzz.hit(card)
                        
            
                    elif pc == 2:
                        zzz.sit()
                        break
                except NameError:
                    print "\nInput either 1 or 2"
                except TypeError:
                    print "\nInput either 1 or 2"
                except SyntaxError:
                    print "\nInput either 1 or 2"
            victor = Bernie_Mac.determine_winner(zzz.hand_score, cowboy.hand_score, gent.hand_score, prep.hand_score)#victor is the assigned name of the output of the dealer's winning scores list
            pot = pot / len(victor)#splits the pot among as many high scores there were (if rwo people got 20, the pot splits and each gets half.  If their was only one winner the pot = the pot / 1, so it doesn't split
            while len(victor) > 0:        
                l = victor.pop()#checks to see who had the winning score and distributes the pot to the winner(s)
                if l == zzz.hand_score:
                    zzz.winnings = zzz.winnings + pot
                elif l == cowboy.hand_score:
                    cowboy.winnings = cowboy.winnings + pot
                elif l == gent.hand_score:
                    gent.winnings = gent.winnings + pot
                elif l == prep.hand_score:
                    prep.winnings = prep.winnings + pot
            os.system('cls')
            print "You've finished the round.  The standings are:"#prints the standings for the user to look at
            print "Lord Havisham has", gent.winnings, "bucks"
            print "Rooster Cogburn has", cowboy.winnings, "bucks"
            print "Eugene Forrester has", prep.winnings, "bucks"
            print zzz.name, "has", zzz.winnings, "bucks"
            file = open(zzz.name + ".txt", "w")#automatically saves the user's profile by overwriting (or creating) a text file for their account
            file.write(zzz.name + "\n" + str(zzz.winnings) + "\n" + "dollars")#writes the information in the user's profile
            file.close()
            with open("High_Scores.txt") as hisc:#checks to see if the user's winnings are higher than the current high score.  If they are the user becomes the new high score
                j = hisc.readlines()
                if zzz.winnings >= int(j[1]):
                    hisc.close()
                    with open("High_Scores.txt", 'w') as file:
                        file.write(zzz.name + "\n" + str(zzz.winnings) + "\n" + "dollars")
                        file.close
            
            while True:#gives the user the option to continue or quit.  The while loop protects in case they enter something other than y or n
                eroc = raw_input("Do you wish to continue? y/n > ")
                if eroc == 'n':
                    os.system('cls')
                    exit()
                elif eroc == 'y':
                    os.system('cls')
                    break
                
                else:
                    print "Your input was not either y or n, please input either y or n"
            if prep.winnings <= 0:
                print "One of the benefits of being a computer generated player is that Eugene gets to stay at the table\nafter he runs out of money"
                prep.winnings = 5#if any of the CPU's runs out of money they get regenerated with 5 bucks.  Otherwise the user might end up being the only player left.  And if the CPU's stay in with negative winnings, the winner of the round can actually lose money (since the pot can be negative)
            if gent.winnings <= 0:
                print "One of the benefits of being a computer generated player is that Lord Havisham gets to stay at the table\nafter he runs out of money"
                gent.winnings = 5#if any of the CPU's runs out of money they get regenerated with 5 bucks.  Otherwise the user might end up being the only player left.  And if the CPU's stay in with negative winnings, the winner of the round can actually lose money (since the pot can be negative)
            if cowboy.winnings <= 0:
                print "One of the benefits of being a computer generated player is that Rooster gets to stay at the table\nafter he runs out of money"
                cowboy.winnings = 5#if any of the CPU's runs out of money they get regenerated with 5 bucks.  Otherwise the user might end up being the only player left.  And if the CPU's stay in with negative winnings, the winner of the round can actually lose money (since the pot can be negative)
            if zzz.winnings <= 0:#if the user runs out of money they get kicked out of the casino
                print "You are out of money and have been kicked out"
                sleep(1)#the user gets a second to read their sentence
                os.system('cls')
                del zzz#the user gets deleted
                break
            from dealer import *
            Bernie_Mac = dealer() #this reinstantiates the dealer so that the deck gets repopulated with the cards that were used that round
            bet_checker = 0#resets the bet checker to make sure the user can't bet 0 dollars
            
Arena = arena()#instantiates the arena object so that this function can be used