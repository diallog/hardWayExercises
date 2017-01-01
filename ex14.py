#!/usr/bin/python

# This is exercise 14 of the Hard Way exercises

from sys import argv

script, userName = argv
prompt = '>> '

print "Hi %s, I'm the %s script." % (userName, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % userName
likes = raw_input(prompt)

print "Where do you live %s?" % userName
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. I'm not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# end script
