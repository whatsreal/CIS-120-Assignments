#Brian Jansen
#Ex 28
#My guesses are in the comments and I got them all right on my first try.

num = 0
num += 1
print num, True and True #1 True
num += 1
print num, False and True #2 False
num += 1
print num, 1 == 1 and 2 == 1 #3 False
num += 1
print num, "test" == "test" #4 True
num += 1
print num, 1 == 1 or 2 != 1 #5 True
num += 1
print num, True and 1 == 1 #6 True
num += 1
print num, False and 0 != 0 #7 False
num += 1
print num, True or 1 == 1 #8 True
num += 1
print num, "test" == "testing" #9 False
num += 1
print num, 1 != 0 and 2 == 1 #10 False
num += 1
print num, "test" != "testing" #11 True
num += 1
print num, "test" == 1 #12 False
num += 1
print num, not (True and False) #13 True
num += 1
print num, not (1 == 1 and 0 != 1) #14 False
num += 1
print num, not (10 == 1 or 1000 == 1000) #15 False
num += 1
print num, not (1 != 10 or 3 == 4) #16 False
num += 1
print num, not ("testing" == "testing" and "Zed" == "Cool Guy") #17 True
num += 1
print num, 1 == 1 and not ("testing" == 1 or 1 == 0) #18 True
num += 1
print num, "chunky" == "bacon" and not (3 == 4 or 3 == 3) #19 False
num += 1
print num, 3 == 3 and not ("testing" == "testing" or "Python" == "Fun") #20 False

# != Not Equal
# <> is another "not equal" operator similar to !=
# > Greater than
# < Less than
# == Equal
# >= Greater than or equal to
# <= Less than or equal to
