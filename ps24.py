#!/usr/bin/python3

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically 
# or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# analysis: possible permutations: num_digits! - 3628800 



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

def compute(num_digits, nth_permutation):
    # digits available for use 
    digits = [i for i in range(num_digits)]

    # currently finding WHAT digit 
    currentFindingDigit = 1 

    # records digit of answer
    answer = ''

    # remaining permutations left to reach nth lexicographic permutation 
    remaining = nth_permutation - 1 



    for i in range(num_digits):
        possiblePermsForDigit = fact(num_digits - currentFindingDigit)
        
        digitIndex = remaining//possiblePermsForDigit
        digit = digits[digitIndex]

        # example:
        # lexicographical permutations:
        # first digit: 0 - 362880 permutations 
        # first digit: 1 - 362880 p 
        # first digit: 2 - 362880 p (1 millionth permutation contained inside) Therefore, first digit is 2 

        answer += str(digit)
        # when digit is used up, it will no longer be taken into consideration 
        digits.remove(digit)

        # moves on to next digit 
        currentFindingDigit += 1 

        remaining -= (possiblePermsForDigit*digitIndex)

    return answer    

if __name__ == "__main__":
    print(compute(10, 1000000))