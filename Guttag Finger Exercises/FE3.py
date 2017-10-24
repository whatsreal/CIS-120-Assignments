#Finger Exercise 3
#End of Chapter 2 Section 4

#Write a program that gets 10 integers from the user.
#Compare those variables and find the largest odd number.
#Print that number or an error message saying that there were none.


#Get the 10 variables.

a = int(input("enter a number"))
b = int(raw_input("enter a number"))
#Can you use a for-loop (or a while-loop) and list?

x, m = [], 0
for i in range(10):
    x.append(int(input("Enter a number")))

for i in x:
    if i % 2 != 0 and i > m:
        m = i

print m
    #test to see if i is odd
        #if it is append to m

    #

m = [1, 3, 39, 5]

#Compare the variables.  Remember the previous FE.  It only had 3 variables.
#This may be far more complex if you do it the same way.  Can you simplify the logic any?






























#Hint keep a record of the largest odd variable you've come across and only compare against that.
#Use a loop.
