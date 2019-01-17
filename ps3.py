#! python3 
#! What is the largest prime factor of the number 600851475143?

# each number can be expressed as a product of its prime factors.
# this solution uses the fact that if you start dividing a number from the 
# smallest possible factor to the largest, all factors will be prime factors and the
# last factor will be the largest possible prime factor 

def compute():
    x = 600851475143
    y = 3 #smallest possible prime factor for x as x is not even 

    # Dividing x by all its prime factors. 
    while x != y:
        while x % y == 0:
            x /= y
        y += 2 #skips even numbers  

    return x

if __name__ == "__main__":
	print(compute())    




