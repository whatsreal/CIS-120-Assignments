#Mason Hunter CIS 120
#Assignment 30 due 2.10.2014
people = 30
cars = 40
buses = 15

if cars>people:
    print"We should take the cars."
elif cars< people:
    print"We should not take the cars."
else:
   print "We can't decide."
  
if buses>cars:
    print "That's too many buses."
elif buses< cars:
    print "Maybe we could take the bus."
else:
    print "We still can't decide."

if people> buses:
    print "Alright, let's just take the buses."
else:
    print"Fine, let's stay home then."
	
if people > buses and cars < buses:
    print "The environment is doing OK" #if there are more people than buses and fewer cars than buses this will be printed
elif people>buses and buses<cars:
#if there are more people than buses and fewer buses than cars this will print
    print "Take public transportation"
else:
#in all other situations this will print
    print "What is going on?"