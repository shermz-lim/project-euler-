#!/usr/bin/python3

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# mathematical source: https://thestarman.pcministry.com/math/rec/RepeatDec.htm

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
    return primes 

# helper function: finds number of recurring digits of 1/p given a prime number p 
# refer to link above for mathematical proof 
def findRecurringDigit(p):
    k = 1 
    while True:
        if (10**k - 1) % p == 0:
            # k will be the number of recurring digits 
            return k
        else:
            k += 1     


def compute():
    # possible values of d to consider: prime numbers up till 1000 
    # 1/prime number will give the largest recurring cycle 

    numbers = findPrimes(1000)
    # 2 and 5 are the only primes without recurring cycles 
    numbers.remove(2)
    numbers.remove(5)

    max_cycle_length = 0 
    max_num = 0 
    # loops through each number and find the recurring cycle of 1/number
    for number in numbers:
        recurring_length = findRecurringDigit(number)
        # if recurring length of current digit is greater than the max, 
        if recurring_length > max_cycle_length:
            # set new max 
            max_cycle_length = recurring_length
            max_num = number

    return (max_cycle_length, max_num)

if __name__ == "__main__":
    print(compute())
    
