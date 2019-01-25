#! python3 
# Find the sum of all the primes below two million.

import sys, time

def compute(n):
	crossed_numbers = set(range(4,n,2))
	total = 2 
	count = 3
	while count < n:		
		total+= count
		count1 = 3
		while count*count1 < n:
			crossed_numbers.add(count*count1)
			count1 +=2
		while True:
			count += 2
			if count not in crossed_numbers:
				break

	return total



if __name__ == "__main__":
	starttime = time.time()
	print(compute(2000000))   
	endtime = time.time() 
	print("Time taken: {}".format(endtime - starttime))