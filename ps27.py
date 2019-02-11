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
# why would it not exceed 100000? greatest k - around 80, greatest b, c - 1000 
# 80^2 + 1000*80 + 1000 = 87400 (still lower than 100000). Hence, the set of 
# primes up till 100000 will be enough to check for all possible values of primes
# that would occur 

def compute():
    primes = findPrimes(100000)
    max_k = 0  
    max_b = 0 
    max_c = 0 

    # for abs(c) in range 1000
    for c in range(-999, 999, 2): # skips even numbers 

        # if constant c is a prime num. c has to be prime to fulfil the first case when n = 0 
        if abs(c) in primes:

            for b in range(-999, 999, 2):
                if abs(b) in primes or abs(b) == 1:
                    # create the quadratic function with b and c 
                    p_func = lambda n: n**2 + b*n + c 
                    k = 0

                    while True:
                        if abs(p_func(k)) in primes:
                            k += 1 
                            continue 
                        else:
                            break  

                    if k > max_k: 
                        max_k = k 
                        max_b = b 
                        max_c = c 

    return (max_b*max_c)

if __name__ == "__main__":
    print(compute())



