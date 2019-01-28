#! python3 
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

numbersFile = open('ps13.txt')

# creates empty list to store numbers
numbers = []
# converting each number in string to a float
for number in numbersFile.readlines():
    number = float(int(number[:-1]))
    numbers.append(number)

print(sum(numbers))