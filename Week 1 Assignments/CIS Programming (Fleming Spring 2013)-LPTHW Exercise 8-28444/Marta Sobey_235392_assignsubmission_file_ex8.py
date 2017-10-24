#Marta Sobey
#Assignment number 8. 1/27/2014

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
#The last line of output uses both single and double quotes because the string "But it didn't sing." used a single-quote as an apostrophe for one of the words which would have made the string print improperly if it had been surrounded by simply single-quotes.
