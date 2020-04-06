#!/usr/bin/env python3.6
import argparse

#build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')

#define the parameters that will be taken by the script
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s 1.0')

#parse and print the arguments passed in by the user
args = parser.parse_args()

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]
    
    for line in lines:
        print(lines.strip()[::1])