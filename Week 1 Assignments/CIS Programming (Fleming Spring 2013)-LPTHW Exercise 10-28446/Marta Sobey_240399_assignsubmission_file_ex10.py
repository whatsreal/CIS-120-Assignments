#Marta Sobey
#Assignment number 10. 1/27/2014

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslach_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslach_cat
print fat_cat

#Using ''' instead of """ allows you to surround strings or other things in double quotes within your list. Other than that, the only thing that makes one better than the other is style preference.

#study drill #3
practice = '''
\\* Marta Sobey
\' I am practicing using different symbols.
\b These are just tests to see how they work.
\t Cool\n\v yeah...
'''

print practice

#study drill #4
first = '''
I say: %r because this is hard.'
''' % "I am \"confused\""
second= """
I say: %s because I am new to this stuff.'
""" % "I \"need\" help"
print first
print second

# %r prints more than %s does. %r is more touchy you could say.