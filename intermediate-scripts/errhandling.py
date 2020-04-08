#!/usr/bin/env python3.6

import argparse

#parser creation
parser = argparse.ArgumentParser(description='Receives a filename and line number to display')

#parser argument defintions
parser.add_argument('file_name', help='The file that will be read from')
parser.add_argument('line_number', help='The line number that will be read from the file')

args = parser.parse_args()

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number - 1]
except IndexError:
    print(f"Error: file '{args.file_name}' doesn't have {args.line_number} lines.")
except IOError as err:
    print(f"Error: {err}")
else:
    print(line)