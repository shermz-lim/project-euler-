#! python3 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import fractions 

def compute():
    LCM = 1 

    for i in range(2, 21):
        LCM = LCM * i/fractions.gcd(LCM, i)

    return LCM     

if __name__ == "__main__":
	print(compute())    