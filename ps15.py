#!/usr/bin/python3

# How many such routes are there through a 20×20 grid - from top left to bottom right?
# Provided that you can only move right and down

# total need 20 moves right, 20 moves down. So question is: how to arrange 20 R and 20 D 
# calculate permutations for :
# 1 - move right , 0 - move down 


# basically 40!/20!/20! combinations - ways of permutations for 20 'down' non-unique objects and 20 'right' non-unique objects
        
def calcFact(x):
    total = 1
    for i in range(1, x + 1):  
        total *= i 
    return total 


if __name__ == "__main__":
    print(calcFact(40)/calcFact(20)/calcFact(20))
    