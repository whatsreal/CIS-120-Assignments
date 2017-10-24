#Marta Sobey
#Assignment number 3. 1/27/2014

#This line simply prints the sentence placed in quotes
print "I will now count my chickens:"
#This line prints what I have in quotes and does the math of 25 added to the result of 30 divided by 6.
print "Hens", 25.0 + 30.0 /6.0
#This line prints what I have in quotes and is then followed by the result of 25 times 3 which is then divided by 4. The result of that math has a remainder of 3 which is the number calculated from the modulus symbol. That number (3) is then subtracted from 100. 
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0
#This line simply prints the sentence placed in quotes
print "Now I will count the eggs:"
#This line prints the sum of 3 added to 2 and added to 1. 5 is then subtracted from that sum (6). The result of 4 modulus 2 (0) can just be disregarded since the result is zero. Next, the result of 1 divided by 4 (.25) is subtracted from the previous sum (1). Finally, 6 is added to that previous sum of 1.
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
#This line simply prints the words inside the quotes followed by the the equation that states the sum of 3 added to 2 is less than 7 subtracted from 5 
print "Is it true that 3.0 + 2.0 < 5.0 - 7.0?"
#This line states that the sum of 3 added to 2 (5) is less than 7 subtracted from 5 (-2). This statement is false, however, so the word "False" is printed by Python
print 3.0 + 2.0 < 5.0 - 7.0
#This line prints the words and numbers that are inside the quotations as they are. This is then followed by the sum of 3 and 2.
print "What is 3.0 + 2.0?", 3.0 + 2.0
#This line prints the words and numbers that are inside the quotations as they are. This is then followed by the result of 7 subtracted from 5.
print "What is 5.0 - 7.0?", 5.0 - 7.0
#This line simply prints the sentence placed in quotes.
print "Oh, that's why it's False."
#This line simply prints the sentence placed in quotes
print "How about some more."
#This line prints the sentence that is within the quotations followed by the word "True" because the statement 5 is greater than -2 is true.
print "Is it greater?", 5.0 > -2.0
#This line prints the sentence that is within the quotations followed by the word "True" because the statement that 5 is greater than or equal to -2 is true.
print "Is it greater or equal?", 5.0 >= -2.0
#This line prints the sentence that is within the quotations followed by the word "False" because the statement five is less than or equal to -2 is false.
print "Is it less or equal?", 5.0 <= -2.0

print "My practice calculation"
print 3 + 2 / 1 - 8 % 6 + 4
#A floating point number is a number that contains a decimal point. For example, 3 is not a floating point number, but 3.0 is.
