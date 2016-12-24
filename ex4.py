#!/usr/bin/python

# This script is an exploration of variables.
# What will make this script more interesting is grabbing the data from another (external) source.

cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
avgPassengersPerCar = passengers / carsDriven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", carsNotDriven, "empty cars today."
print "We can transport", carpoolCapacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", avgPassengersPerCar, "in each car."

# end script
