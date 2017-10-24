#Dan Fleming
#Lucky Number Program
#From Class 2

from os.path import exists
#from sys import argv

#Checks to see if filename exists.
#if it does open with append ('a')
#otherwise open to write ('w')
def CheckAndOpen(filename):
    if(exists(filename)):
        return open(filename, 'a')
    else:
        return open(filename, 'w')

#Accepts a variable number of inputs. 
#Converts those to integers
#outputs the integers as a list.        
def ConvertToInt(*inputvars): #I'm doing something weird here
    outputvars = [] #and here
    for i in inputvars: #and more stuff you don't know here
        outputvars.append(int(i)) #You don't know this yet either
    return outputvars
    

#This block was our first attempt at getting information from the user
#I am using prompts and raw_input() for this:
#firstNum = raw_input("What is your height? ")
#secondNum = raw_input("How old are you? ")
#thirdNum = raw_input("What is your shoe size? ")

#This was our second way to get information from the user
#Here I use the arguments to input 3 data items.
#remember to un-comment the "from sys import argv" line if you are running this section.
#also, remember that the first element is the script name (ie the name of this file)
#so we need to get that out.
#scriptName, firstNum, secondNum, thirdNum = argv

#This is the third way we can get information from a user
#this one opens a file.
#first ask the user for a filename
myFileName = raw_input("What file can I pull your numbers from? ")

#Now, we'll open the file
#Because I didn't provide a second option it opens to read.
myFile = open(myFileName)

#Now let's get the numbers into variables.
#We assume one number per line.
firstNum = myFile.readline()
secondNum = myFile.readline()
thirdNum = myFile.readline()


#Remember to close the file.
myFile.close()


#Convert the variables we have to integers!
#See the comments above the function definition for more information
firstNum, secondNum, thirdNum = ConvertToInt(firstNum, secondNum, thirdNum)

#Now lets do the math to get the lucky number.
luckyNumber = firstNum * secondNum / thirdNum

#Now tell the user
print "Your lucky number is %r!" % luckyNumber

##############
#Below this I am doing some exercises we didn't get time to do in class.
#Make sure you understand what is going on as it will help you on your homework
##############



#Let's keep a record of each person's lucky numbers in a file.

#So let's ask for a name:
userName = raw_input("What is your name? ")

#convert the name to a proper file name with a .txt extension
userName += ".txt"
#WHAT DID YOU DO?!?! 
#The line above is the same as writing: userName = userName + ".txt"
#Just shorter.  (trust me)

#Open the file checking to see if it exists.
#Lucky we have a function to do that.
#For more info see the above function.
userRecord = CheckAndOpen(userName)

#Now append the user's newest lucky number to the file
userRecord.write("%d\n" % luckyNumber)

#Don't forget to close the file!
userRecord.close()

#Just for fun lets read all the previous lucky numbers:
readOnlyFile = open(userName)
print "All your lucky Numbers are:"
print readOnlyFile.read()