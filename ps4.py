#! python3 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# function checks whether a number expressed as a string is palindrome 
def isPal(x):
    if len(x) <= 1:
        return True 

    if x[0] == x[-1]:
        return isPal(x[1:-1])

    else:
        return False     

def compute():        
    palindromes = []        
    for x in range(900, 999):
        for y in range(900, 999):
            product = x * y 
            if isPal(str(product)):
                palindromes.append(product)
    return max(palindromes)            

if __name__ == "__main__":
    print(compute())