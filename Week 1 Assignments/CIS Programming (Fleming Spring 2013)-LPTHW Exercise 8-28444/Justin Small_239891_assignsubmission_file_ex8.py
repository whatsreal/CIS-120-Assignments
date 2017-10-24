# Justin Small 1/25/2014

# this line defines formatter as the combination of four strings %r
formatter = "%r %r %r %r"

# this line prints variable formatter defined by strings (1, 2, 3, 4) 
print formatter % (1, 2, 3, 4)
# this line prints variable formatter defined by strings ("one", "two", "three", "four")
print formatter % ("one", "two", "three", "four")
# this line prints variable formatter defined by strings (True, False, False, True_
print formatter % (True, False, False, True)
# this line prints variable formatter difined by string (formatter, formatter, formatter, formatter)
print formatter % (formatter, formatter, formatter, formatter)
# this line prints variable formatter difined by string ("I had this thing,", "That you could type up right.", "But it didn't sing.", "So I said goodnight.") 
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
