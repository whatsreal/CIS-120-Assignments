#Marta Sobey
#Assignment Number 12. 2/10/14

#These lines print what are inside quotes followed by an opportunity for the user to insert there own information stored under the respective variable (age, height, or weight).
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

#This line prints what is inside quotes while replaces the %r characters with the content assigned to age, height, and weight respectively
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#Study Drill number 1 says... Help on built-in function raw_input in module __builtin__:
#Pydoc is used for looking at and generating Python documentation
#python -m pydoc open/file/os/sys