def add(a,b):
    print(f"ADDING {a} + {b}")
    return(a + b)

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return(a - b)

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return(a * b)

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return(a/b)

print("Let's do some math functions!")

age = add(20,4)
height = subtract(86,11)
weight = multiply(105,2)
iq = divide(10,10)

print(f"AGE: {age}, HEIGHT: {height}, WEIGHT: {weight}, IQ: {iq}")