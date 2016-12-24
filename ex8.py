#!/usr/bin/python

# Exercise 8: printing, it's important...your progreams have to express what they accomplish :-)

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# print formatter % (True, False, False, True)
print formatter % ("True", "False", "False", "True") # true/false as strings rather than the python recognized key words
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# end script
