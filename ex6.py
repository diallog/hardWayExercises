#!/usr/bin/python

# Exercise 6: more with strings and text

x = "There are %d types of people in the world." % 10
binary = "binary" # a variable containing a string
doNot = "don't" # another variable with another string
y = "Those who know %s and those who %s." % (binary, doNot) # a variable containing a string that then incorporates the values of two other variables

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"

print jokeEvaluation % hilarious # have to look at the value of jokeEvaluation to see that it is a string that makes room for the the inclusion of the variable 'hilarious'.

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# end script
