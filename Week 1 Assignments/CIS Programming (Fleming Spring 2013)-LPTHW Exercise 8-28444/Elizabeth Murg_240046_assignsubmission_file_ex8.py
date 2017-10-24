#Elizabeth Murg
#Assignment Number 8. 11/27/14

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
) 
#I can't figure out why the last line of output uses both single-quotes and double-quotes too. 
