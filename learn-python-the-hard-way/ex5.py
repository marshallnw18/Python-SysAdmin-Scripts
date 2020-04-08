#!/bin/usr/env python3.6

my_name = 'Nick Marshall'
my_age = 24 #not a lie
my_height = 75 #inches
my_weight = 210 #lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s" % my_name) #Older formatting
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair") #Python3 formatting
print("His teeth are usually %s depending on the coffee", my_teeth)

print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {my_age + my_height + my_weight}")