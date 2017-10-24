#this is the file through which the whole game runs
from arena import *
os.system('cls')#this command is used (alot) and is just to clear the screen and make the game look prettier

while True:#just so that the menu won't stop running unless the user uses a quit option
    print """
Welcome to BlackJack, what would you like to do?
    1.) Play with a new profile
    2.) Load an existing profile and play
    3.) Learn How to Play
    4.) View High Scores
    5.) Quit"""
    x = raw_input("Please input a number (i.e 7 not 'seven') to select your choice  > ")
    if x == '1':
        os.system('cls')
        print "You are entering the ring, this is your last chance to turn back until the end of the next game.  \nIf you wish to turn back press q "
        s = raw_input("> ")
        if s == 'q':#this gives a new user one last chance to quit- in case they don't know what they're getting into
            os.system('cls')
            continue#if they choose to quit the program goes back to main menu
        else:    
            os.system('cls')
            x = raw_input("What is your name? > ")
            zzz = human_player()#creates a new human_player
            zzz.name = x#assigns the raw_input name as the human player's name
            print """Your opponents are:
        Lord Havisham: 
            A suave British gentleman.  He is good at seemingly
        everything (including 14 forms of Martial Arts).  He is classy, cool under
        pressure, and is quite the ladies man.  We're not saying he is a spy, but 
        we wouldn't be suprised if he was. His favorite activities include long walks
        on the beach, playing polo, and attending the symphony.\n\n\n\n\n\n\n\n\n\n\n\n
        Rooster Cogburn: 
            Rooster is a rough and tumble cowboy.  He lost his eye in a 
        fight a few years ago after another BlackJack player insulted him 
        (That fight actually occurred at this very table).  He is not afraid to
        take a risk, he has a dog named Rusty, and he's a man's man.\n\n\n\n\n\n\n\n\n\n\n\n
        Eugene Forrester: 
            Eugene is a brat.  He is currently a junior at Harvard, and he won't let
        anyone forget about it.  His parents are multi millionaires and they 
        spoiled Eugene rotten as a child.  He is pretentious, stuffy, afraid of risks,
        and he thinks all the girls are into him (which they're not).  He'll probably 
        end up being the CEO of a fortune 500 company one day, but nobody likes him,
        so who cares.
  
Press enter to begin the game
        """
        raw_input()
        os.system('cls')
        Arena.play(zzz, prep, cowboy, gent, Bernie_Mac)#the arena function is where the game action takes place.  The arena function takes the players and dealer as arguments  
    
    elif x == '2':
        os.system('cls')
        yyy = raw_input("What is the name of your profile? > ") + ".txt"#this takes a user input and opens their file
        
        try:
            with open(yyy) as file:
                zzz = human_player()
                j = file.readlines()#creates a list of the lines of the file
                zzz.name = j[0]#the first item in this list (the first line) is the name
                zzz.name = zzz.name[:-1]#this is to remove the newline character at the end of the name line
                zzz.winnings = int(j[1])#the second item in the list (second line of the file) is the winnings
                
        except:
            print "That file name was not found"
            continue#if the file did not exist this prints and it goes back to the main menu
        os.system('cls')
        print """Your opponents are the usual suspects:
        Lord Havisham: 
            A suave British gentleman.  He is good at seemingly
        everything (including 14 forms of Martial Arts).  He is classy, cool under
        pressure, and is quite the ladies man.  We're not saying he is a spy, but 
        we wouldn't be suprised if he was. His favorite activities include long walks
        on the beach, playing polo, and attending the symphony.\n\n\n\n\n\n\n\n\n\n\n\n
        Rooster Cogburn: 
            Rooster is a rough and tumble cowboy.  He lost his eye in a 
        fight a few years ago after another BlackJack player insulted him 
        (That fight actually occurred at this very table).  He is not afraid to
        take a risk, he has a dog named Rusty, and he's a man's man.\n\n\n\n\n\n\n\n\n\n\n\n
        Eugene Forrester: 
            Eugene is a brat.  He is currently a junior at Harvard, and he won't let
        anyone forget about it.  His parents are multi millionaires and they 
        spoiled Eugene rotten as a child.  He is pretentious, stuffy, afraid of risks,
        and he thinks all the girls are into him (which they're not).  He'll probably 
        end up being the CEO of a fortune 500 company one day, but nobody likes him,
        so who cares.
Press enter to begin the game
        """
        raw_input()
        os.system('cls')
        Arena.play(zzz, prep, cowboy, gent, Bernie_Mac)#passes in the players and dealer and starts the game
    
    elif x =='3':
        os.system('cls')
        print """Here are the basic rules of 21:
        Each player is dealt two cards in the form of [(card name), (card value)].  
        The goal of the game is to get your hand to equal as close to 21 as 
        possible without going over.  After each player has two cards, each
        player may choose to 'hit' (meaning receive another card to increase
        their score but at the risk of exceeding 21) or 'sit' and stay with the
        cards you already have.  All numbered cards have a value equal to their
        number, and all face cards have a value of 10.  An ace is an exception as
        it can count for either a 1 or a 10.  You decide which it will be when you are dealt
        the ace, and once you decide you can't change your mind.
        The way that this casino works is that at the beginning of each round
        you must place a wager. Then the winner (the person closest to 21) will win
        the pot.  If two or more people win they split the pot.  You cannot end
        in the middle of hand, or save in the middle of a hand.  But between
        rounds you are free to do so.  Each player has a profile, high scores
        are determined by the highest overall profile winnings amount. 
        """
        end = raw_input("To return to the main menu press enter")#lets the user decide when to return to the main menu
        os.system('cls')
        
    elif x == '4': #displays the high scores -which are stored in a text file
        os.system('cls')
        with open('High_Scores.txt', 'r') as file:
            print file.read()
        raw_input("\nPress enter when you wish to return to the main menu")#lets the user decide when to return to the main menu
        file.close
        os.system('cls')
    elif x == '5':#gives the user the option to quit the program
        os.system('cls')
        exit()