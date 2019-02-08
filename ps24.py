#!/usr/bin/python3

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically 
# or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# analysis: possible permutations: 10! - 3628800 



# 2013456789 - 725761 th permutation 
# second digit: 

# helper function - factorial 
def fact(n):
    total = 1 
    for i in range(1, n+1):
        total *= i 
    return total     

# this algorithm finds the millionth lexicographic permutation by determining each digit of the permutation
# from the first to last digit. As it is in lexicographic order, the digits can be determined 

# digits available for use 
digits = [i for i in range(10)]

# currently finding WHAT digit 
currentFindingDigit = 1 

# records digit of millionth_permutation
millionth_permutation = ''

# remaining permutations left to reach 1 millionth lexicographic permutation 
remaining = 999999



for i in range(10):
    possiblePermsForDigit = fact(10 - currentFindingDigit)
    
    digitIndex = remaining//possiblePermsForDigit
    digit = digits[digitIndex]

    # example:
    # lexicographical permutations:
    # first digit: 0 - 362880 permutations 
    # first digit: 1 - 362880 p 
    # first digit: 2 - 362880 p (1 millionth permutation contained inside) Therefore, first digit is 2 

    millionth_permutation += str(digit)
    # when digit is used up, it will no longer be taken into consideration 
    digits.remove(digit)

    # moves on to next digit 
    currentFindingDigit += 1 

    remaining -= (possiblePermsForDigit*digitIndex)

print(millionth_permutation)    