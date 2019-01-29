#!/usr/bin/python3 

import math

def isPerfectSquare(x):
    """given x: a positive int,
    checks whether x is a perfect square
    
    returns: boolean (True/False) """
    sqrt = math.sqrt(x)
    if x % sqrt == 0:
        return True 
    return False 

def compute():
    for a in range(1, 500):
        for b in range(a, 500): # b > a
            # if a**2 + b**2 gives a perfect square
            c_square = a**2 + b**2
            if isPerfectSquare(c_square):
                # obtain c 
                c = int(math.sqrt(c_square))
                # if a + b + c is equal to 1000, they are the set of pythagorean triplet
                if a + b + c == 1000:
                    # returns product abc 
                    return str(a*b*c)

if __name__ == "__main__":
    print(compute())