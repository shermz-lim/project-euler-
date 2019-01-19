#! python3 
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def compute(N):
    """
    N: an integer 
    Returns: difference between sum of squares of N natural numbers and square
    of the sum 
    """

    sum_of_squares = 0
    for i in range(1, N + 1):
        sum_of_squares += i**2

    square_sum = 0 
    for i in range(1, N + 1):
        square_sum += i 
    square_sum = square_sum ** 2

    return square_sum - sum_of_squares

if __name__ == '__main__':
    print(compute(100))