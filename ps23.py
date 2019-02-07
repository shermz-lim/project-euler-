#!/usr/bin/python3 

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the 
# sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by 
# analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant 
# numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from itertools import combinations_with_replacement 

# helper function - find divisors of a number 
def findDivisors(n):
    """ n: int
    returns: set of divisors """

    # initialize divisors list. includes 1 as it is a divisor of all numbers
    divisors = set({1})
    # for positive integers up till square root of n,
    for i in range(2, int(n**0.5) + 1):
        # if n is divisible by integer
        if n % i == 0:
            # integer will be a divisor of n 
            divisors.add(i)
            # n divided by integer will also be a divisor of n 
            divisors.add(n//i)
    return divisors 

# checks whether a number is abundant
def isAbundant(n):
    divisors = findDivisors(n)
    if sum(divisors) > n:
        return True 
    else:
        return False     

def compute():
    # finds all abundant number up till 28123
    abundant_numbers = []
    for number in range(1, 28124):
        if isAbundant(number):
            abundant_numbers.append(number)
    # abundant numbers contains all abundant numbers up till 28123

    # create a set of possible sums of abundant numbers up till 28123 
    sums_of_abundant_numbers = set(sum(pair) for pair in combinations_with_replacement(abundant_numbers, 2) if sum(pair) < 28123)
    
    # sum of positive integers which cannot be written as sum of two abundant numbers = 
    # sum of positive int from 1 to 28123 minus sums_of_abundant_numbers
    total_sum = sum(range(1, 28123)) - sum(sums_of_abundant_numbers)
    return total_sum

if __name__ == "__main__":
    print(compute())