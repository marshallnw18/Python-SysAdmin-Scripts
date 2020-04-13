#!/bin/usr/env python3.6

def print_two(arg1, arg2):
    print(f"arg1: '{arg1}', arg2: '{arg2}'")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin.")

print_two("Nick", "Marshall")
print_one("First!")
print_none()

