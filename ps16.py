#!/usr/bin/python3 

# What is the sum of the digits of the number 2**1000?

def compute():
    total = 0
    for digit in str(2**1000):
        total += int(digit)
    return total    

if __name__ == "__main__":
    print(compute())  