#Mason Hunter CIS 120
#Assignment 23 due 2.10.0214
import re, collections #This line imports the two arguments re and collections

def words(text): return re.findall('[a-z]+', text.lower()) #here the words function is defined, and the oujtpute will be re.findall

def train(features): #train function is defined
    model = collections.defaultdict(lambda: 1) #the variable model is declared
    for f in features: # he makes a "for loop" for f and features
        model[f] += 1 # says that model = model + 1
    return model #model is what the function will kick out

NWORDS = train(words(file('big.txt').read())) # the variable nwords is the output of the file function run through the words function run through the train function

alphabet = 'abcdefghijklmnopqrstuvwxyz' # assignns the variable alphabet

def edits1(word): #defines the edits function
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)] #more complicated variables, I don't understand a lot of this
   deletes    = [a + b[1:] for a, b in splits if b]#more complicated variables, I don't understand a lot of this with for and or commands
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]#more complicated variables, I don't understand a lot of this
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]#more complicated variables, I don't understand a lot of this
   inserts    = [a + c + b     for a, b in splits for c in alphabet]#more complicated variables, I don't understand a lot of this
   return set(deletes + transposes + replaces + inserts) #returns whatever those variables meant through the set funciton

def known_edits2(word): #another function
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)#and its output

def known(words): return set(w for w in words if w in NWORDS)#another function

def correct(word):#another function
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]#more variables that use the output of previous functions
    return max(candidates, key=NWORDS.get)def words(text): return re.findall('[a-z]+', text.lower()) #returns a corrected word by running the known word through previously defined functions


def train(features): #defines the train function with the features variable
    model = collections.defaultdict(lambda: 1) #defines the model variable
    for f in features:
        model[f] += 1
    return model # outputs a new value for model within this function

NWORDS = train(words(file('big.txt').read())) #declares the nwords variable
def edits1(word):#a new edits function for the inputted word 
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]#this is the splits variable
   deletes    = [a + b[1:] for a, b in splits if b]#this is the deletes variable
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]#this is the transposes variable
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]#this is the replaces variable
   inserts    = [a + c + b     for a, b in splits for c in alphabet]#this is the inserts variable
   return set(deletes + transposes + replaces + inserts) #returns all the previous variables through the set function
   def known(words): return set(w for w in words if w in NWORDS) #runs that return through some more functions

def correct(word):#defines the correct function
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word] #declares the candidates variable
    return max(candidates, key=NWORDS.get)#returns the maximum from candidates to key