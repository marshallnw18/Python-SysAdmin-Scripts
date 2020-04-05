#!/usr/bin/env python3.6

name = input("What is your name? ")
birthdate = input("What is your birth date? ")
#cast to an integer because "input" will return a string
age = int(input("How old are you? "))

print(f"Your name is {name}")
print(f"You were born on {birthdate} and you are {age} years old.")

def age_add(age):
    return(age + 5)

print(f"In five years, you will be {age_add(age)} years old.")


