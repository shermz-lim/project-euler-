
# function finds prime numbers using the sieve algorithm 
# N is the limit 
def compute(N):
    nums = [x for x in range(2, N)]
    p = 2 
    while len(nums) >= 1:
        for num in nums:
            if num % p == 0:
                nums.remove(num)
        for num in nums:
            p = num
            break
    return p 

print(compute(16000000))