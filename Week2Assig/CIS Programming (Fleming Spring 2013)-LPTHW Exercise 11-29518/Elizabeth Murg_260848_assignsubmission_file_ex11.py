#Elizabeth Murg
#Assignment Number 11. 2/5/2014.

#this block will ask a question in string format and then the user will input an answer to the question. Each answer will be linked to a variable.
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#This block will print out a final statement in response to the questions asked inputting the answers given by the user into the sentence using %r and each assigned variable.
print "So you're %r old, %r tall and %r heavy." % (age, height, weight)

#in Python 2, raw_input() will return a string, but input() will try to run what has been given as a Python expression
#raw_input() takes what the user typed and gives it back, but input() actually has an evaluation performed on it.

#sample of raw_input() from cyberciti.biz
#this block will assign the variable to the raw_input and ask for a name. 
#Then the next line will print a response using the input assigned to the variable "name"
#the difference is that this form just uses raw_input for all the prompting instead of putting raw_input on a different line than the prompt
name = raw_input ('Enter your name : ')
print ("Hi %s, let's be friends!" % name);

#my own form will do basically the same thing that the previous two forms did. 
print "What is your favorite color?",
color = raw_input()
print "What is your favorite animal?",
animal = raw_input() 
print "What is your favorite sport?",
sport = raw_input()
print "Dan's favorite color is %r. His favorite animal is the %r, and his favorite sport is %r." % (color, animal, sport)

#'6\'2"' probably has the \' because we inserted an apostrophe in the middle of a string already enclosed in apostrophes and the number itself because of the %r was enclosed in parantheses
