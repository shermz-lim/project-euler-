#!/usr/bin/python3 

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# 1x1 square edge, 3x3 square edge, 5x5 square edge, 7x7 square edge ... 1001 x 1001 square edge 



def compute():
    # total is the count of the sum 
    total = 1
    # current num is to keep count of the current number being added to total 
    current_num = 1  

    # loops through each square edge from 3x3 to 1001x1001
    for currentSquareEdge in range(3, 1002, 2):
        # when enter new square edge, current number will increment by (currentSquareEdge - 1) four times 
        increment = currentSquareEdge - 1
        for _ in range(4):
            current_num += increment
            # add current number to total 
            total += current_num

    return total         

if __name__ == "__main__":
    print(compute())
