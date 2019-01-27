#! python3 
# What is the value of the first triangle number to have over five hundred divisors?

import math, itertools


def compute():
	triangle = 0
	i = 1 

	while True:
		triangle += i 
		i += 1 
		if num_divisors(triangle) > 500:
			return str(triangle)


# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
	end = math.sqrt(n)
	result = sum(2
		for i in range(1, int(end) + 1)
		if n % i == 0)
	if end**2 == n:
		result -= 1
	return result


if __name__ == "__main__":
	print(compute())