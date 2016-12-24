#!/usr/bin/python

# Exercise 11: get that input...

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %s tall and %r heavy." % (
    age, height, weight)

# Interesting observation: when providing the input to the variables, if you include a non-printing character like \t and then print that variable using %r, the script output will show the '\t'. Good stuff.

# end script
