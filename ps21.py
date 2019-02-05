#!/usr/bin/python3

# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.

# Evaluate the sum of all the amicable numbers under 10000.

# function to calculate the sum of divisors of a number
def sumDivisors(n):
    # includes 1 
    divsSum = 1 
    # find divisors from 2 to square root of n 
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            # if divisor is a divisor, n/divisor will be a divisor too 
            divsSum += (divisor + n/divisor)
    # if n is a perfect square, remove one of the duplicate divisor
    # that is the square root of n 
    if n == (int(n**0.5))**2:
        divsSum -= n**0.5       
    return int(divsSum)

def compute():
    limit = 10000
    amicableSums = 0 

    # find amicable numbers by checking all numbers from 2 to 10000 (exclusive)
    for i in range(2, limit):
        # b = d(i)
        divsSum = sumDivisors(i) 
        # checks whether d(d(i)) == i 
        if sumDivisors(divsSum) == i:
            # only qualify as an amicable number if a ≠ b  i.e. i != divsSum 
            if i != divsSum:
                amicableSums += i 

    return amicableSums       

if __name__ == "__main__":
    print(compute())
            
