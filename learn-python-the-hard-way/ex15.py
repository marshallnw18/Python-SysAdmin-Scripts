#!/bin/usr/env python3.6

from sys import argv

script = argv[0]
filename = argv[1]

#open a designated file for reading and print the contents
txt = open(filename, 'r')
print(f"Here's your file, '{filename}': ")
print(txt.read())

#perform the same action with input rather than terminal argument
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again, 'r')
print(txt_again.read())