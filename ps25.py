#!/usr/bin/python3

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# finds the nth fibonnaci term 
def fib(n):

    current, following = 1, 1
    # index - term of current fibonnaci number 
    index = 1 
    while index < n:
        current, following = following, current+following
        index += 1 

    return current  

def compute():
    # loops until fibonnaci number with 1000 digits is found 
    index = 1 
    while True:
        fibonnaci_term = fib(index)
        # checks whether fibonnaci number has 1000 digits 
        if len(str(fibonnaci_term)) == 1000:
            break 

        # finds next fibonnaci number
        index += 1 

    # returns index of fibonnaci number w 1000 digits 
    return index 

if __name__ == "__main__":
    print(compute())
