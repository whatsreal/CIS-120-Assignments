#Brian Jansen
#Ex 13

from sys import argv

script, first, second, third = argv

#Study Drill Script.  The below lines make it so that the script would have less arguments and then more, respectively. 
#script, first, second = argv
#script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print raw_input("Who's your daddy? ")  #Study Drill Yo!
print "Right!  Your father is your daddy..."

#If you don't give it enough variables to unpack, then it gives an error that essentially tells you that.

