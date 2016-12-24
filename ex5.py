#!/usr/bin/python

#Exercise 5: more variables and printing

myName = 'Zed A. Shaw'
myAge = 35 # in-stream comment just for giggles
myHeight = 74 # in inches
myWeight = 180 # in pounds
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'

# now for some print statements in a new format

print "Let's talk about %r for a minute." % myName
print "He's %X inches tall." % myHeight
print "He weighs %d pounds, or if you prefer %d kilos." % (myWeight, myWeight * 0.453592)
print "Not so heavy is he."
print "He's got %s eyes and %r hair." % (myEyes,myHair)
print "His teeth are usually %s depending upon whether or not he's had coffee recently." % myTeeth

# putting multiple together

print "If I add %d, %d, and %d, I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)

# end script
