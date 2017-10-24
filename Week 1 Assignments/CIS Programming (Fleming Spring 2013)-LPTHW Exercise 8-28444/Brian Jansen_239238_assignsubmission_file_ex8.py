#Brian Jansen
#Ex 8

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) #This crap is sneaky, gotta have the first letter capital or it thinks it's a variable.  Almost had to do that error write down thing...but not this day!
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight." #Huh?
	) # <-- Shouldn't this be indented?  
