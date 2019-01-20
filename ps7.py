#! python3 
# What is the 10 001st prime number?

import sys

# function checks whether a number is prime using an array of prime factors smaller than the number:
def isPrime(arr, num):
    for primeNum in arr[:len(arr)//2]:
        if num % primeNum == 0:
            return False 
    return True         


# function finds the Nth prime number 
def compute(N):
    # Starts finding prime numbers from 3. 1st prime - 2 - is appended in primeNums and no. of prime is already 1 
    primeNums = [2]
    primeCount = 1
    num = 3

    while primeCount < N: 
        statement = "Testing number: {}".format(num)
        sys.stdout.write(statement + "\b"*len(statement))
        if isPrime(primeNums, num):
            primeNums.append(num)
            primeCount += 1
        num += 2 

    return primeNums.pop()       

if __name__ == "__main__":
    N = int(input("Enter the Nth prime number you want to find: "))
    print("\n" + "The {}th prime number is ".format(N) + str(compute(N)))    