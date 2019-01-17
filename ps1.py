#! python3 
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def compute():
    total = 0 
    # loops through all numbers till 1000 
    for i in range(3, 1000):
        # if number is a multiple of 3 or 5 or both, add it to total
        if i % 3 == 0 or i % 5 == 0:
            total += i 
    return str(total)        


if __name__ == "__main__":
	print(compute())