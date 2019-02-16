#!/usr/bin/python3 

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits. 

def compute():
    valid_numbers = []

    for number in range(10, 300000):
        total = 0 
        for digit in str(number):
            total += (int(digit))**5
        if total == number:
            valid_numbers.append(number)

    return sum(valid_numbers)   

if __name__ == "__main__":
    print(compute())    