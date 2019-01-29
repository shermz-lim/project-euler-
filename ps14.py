#!/usr/bin/python3

#The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# calculating chain length for all odd numbers from 100001 to 1000000
max_count = 0 
max_num = 0 
for i in range(1, 1000000, 2):
    count = 0 
    current_num = i 
    while current_num != 1:
        if current_num % 2 == 0:
            current_num /= 2
            count += 1 
        else:    
            current_num = current_num*3 + 1
            count += 1 
    if count > max_count:
        max_count, max_num = count, i 
print("{} produced chain with longest length of {}".format(max_num, max_count))        



