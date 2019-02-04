#/usr/bin/python3

# Find the sum of the digits in the number 100!

def compute(n):
    def fact(n):
        answer = 1 
        for i in range(1, n+1):
            answer *= i 
        return answer

    digit_sum = 0 
    for digit in str(fact(n)):
        digit_sum += int(digit)

    return digit_sum

if __name__ == "__main__":
    print(compute(100))