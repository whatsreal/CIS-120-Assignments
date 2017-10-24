#Elizabeth Murg 
#Assignment Number 26. 2/9/2014

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#This line is missing the colon after (words). Also, pop was spelled poop
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

#This line was missing a paranthesis after the number -1
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#explanation was spelled wrong (explantion)
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation 
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

#the six was originally a five which didn't add up to 5
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
	#line 65 used the wrong backslash
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#double equal sign changed to single equal and hyphen for start-point changed to start_point
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
#changed jeans to beans
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#changed crabapples to crates, point was spelled pont and missing final paranthesis
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#line 82 misspelled the sentence (good, wait, and didn't put a space between good \t and things."
sentence = "All good things come to those who wait."

#line 89 originally read words= ex25.break_words(sentences) but I took out the ex25. because you only need to write that if you are in the powershell
words = break_words(sentence)
#same with line 91
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
#there was a period in front of print in line 96; took it out
print_first_word(sorted_words)
print_last_word(sorted_words)
#took out another ex25. in line 99
sorted_words = sort_sentence(sentence)
#line 101 print was spelled prin (changed that too)
print sorted_words

#This line has the first spelled as irst
print_first_and_last(sentence)
#This next line had the 'and' and the 'sentence' misspelled and an unnecessary tab
print_first_and_last_sorted(sentence)
