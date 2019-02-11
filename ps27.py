#!/usr/bin/python3 
# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, starting with n=0.

# e.g. n2+n+41 has k consecutive prime numbers. if p(n) is such a quadratic expression, p(n-k) will be 
# such a quadratic expression too . Constant value has to be a prime number too. p(n-k) will then produce 
# 2k of such consecutive prime numbers 

# helper function: returns a list of prime numbers up till value of n 
def findPrimes(n):
    primes = [2]
    current_number = 3 
    while current_number < n:
        isPrime = True  
        for prime in primes:
            if current_number % prime == 0:
                isPrime = False
                break 
        if isPrime:
            primes.append(current_number)
        current_number += 2
    return set(primes)

# used to check the consecutive prime numbers produced by function and 
# the value of the constant c of quadratic expression 
primes = findPrimes(100000)
max_k = 0  
max_b = 0 
max_c = 0 

for c in range(-1000, 1000):
    # checks for p(n)
    # if constant c is a prime num
    if c in primes or -c in primes:
        for b in range(-1000, 1000):
            # create the quadratic function with constant c 
            p_func = lambda n: n**2 + b*n + c 
            n = 0

            while True:
                if p_func(n) in primes or -p_func(n) in primes:
                    n += 1 
                    continue 
                else:
                    break  

            if n > 10:
                print(n, b, c)



