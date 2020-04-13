#!/bin/usr/env python3.6

from sys import argv
from os.path import exists

script = argv[0]
from_file = argv[1]
to_file = argv[2]

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file, 'r').read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C (^C) to abort.")

input("?")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()