#!/usr/bin/python

# Exercise 7: enough printing already

print "Mary had a little lamb. ",
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what's going to happen here?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# here's a curve ball...whatch the comma at the end. If you don't understand what's happening, then remove it.

print end1 + end2 + end3 + end4 + end5 + end6, # the comma overides the \n so that the next print statment follows immediately rather than on the next line.
print end7 + end8 + end9 + end10 + end11 + end12
