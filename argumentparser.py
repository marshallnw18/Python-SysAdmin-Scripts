#!/usr/bin/env python3.6
import argparse

#build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')

#define the parameters that will be taken by the script
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args) 

#parse the arguments

#read the file, reverse the contents, and print

