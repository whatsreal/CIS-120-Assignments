#Elizabeth Murg
#Assignment Number 10. 1/27/14

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#fun code: I tried it and it made a little symbol that would flash back in forth between the symbols I typed.
#I commented it out because I couldn't type anything more into my powershell...
#while True: 
	#for i in ["/","-","|","\\","|"] : 
		#print "%s\r" % i, 

#using single triple quotes makes no difference
fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print fat_cat2

#study drill #3
justmessing = '''
\\* Betty
\' I don't know what I'm doing
\b I'm just trying study drill 3
\t How fun!\n\v Sort of...
'''
print justmessing

#study drill #4
b = '''
Betty said: %r because I am a student.'
''' % "I \"need\" to study"
b2= '''
Betty said: %s because I am a student.'
''' % "I \"need\" to study"
print b
print b2

 




