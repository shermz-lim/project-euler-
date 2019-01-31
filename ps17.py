#!/usr/bin/python3

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# different variations:
# 1 to 10: one to ten
# 11 to 20: eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, 
# 21 to 99: _ _ 2 digits: 1st digit: twenty, thirty etc. 2nd digit: reuse 1 to 10. e.g. twenty-one, twenty-two, twenty-three, thirty-one, 
# 100: _ _ _ 3 digits: 1st digit: one to ten + hundred. 2nd and 3rd digit: reuse 11 to 99.   one hundred, two hundred etc. 
# 1000 : one thousand 

# Defining dictionaries that maps numbers to letters:
numbers_to_letters = {
    # one to nineteen (special)
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 
    # twenty to ninety  
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80:'eighty', 90:'ninety'
}

def compute():
    total_letters = 0 

    # helper function countTwoDigits(number)
    def countTwoDigits(number):
        """number: from 20 to 99
            returns: total letters count"""
        total_letters = 0     
        # count digit in ones place:
        ones = number % 10 
        total_letters += len(numbers_to_letters[ones])

        # count digit in tens place:
        tens = number - ones 
        total_letters += len(numbers_to_letters[tens])
        return total_letters

    for number in range(1, 1001):
        # counting letters for special numbers from 1 to 19
        if number >= 1 and number <= 19:
            total_letters += len(numbers_to_letters[number])

        # counting letters for numbers 20 to 99
        elif number <= 99:
            total_letters += countTwoDigits(number)
        
        # count letters for numbers in hundreds:
        elif number <= 999:    
            # e.g. one hundred and ninety-nine : 199

            # counting numbers in tens and ones place
            tens_and_ones = number%100
            if tens_and_ones >= 0 and tens_and_ones <= 19:
                total_letters += len(numbers_to_letters[tens_and_ones])
            else:
                total_letters += countTwoDigits(tens_and_ones)    
            if tens_and_ones != 0:
                # counting letter 'and' only if tens and ones is not zero. therefore, number is not one hundred, two hundred etc. 
                total_letters += 3 

            # count hundreds
            # adding word 'hundred'
            total_letters += len('hundred')
            # adding digit in hundreds place 
            hundreds_digit = (number - tens_and_ones)/100
            total_letters += len(numbers_to_letters[hundreds_digit])

        else: # when number = 1000 
            total_letters += len('onethousand')    

    # returns total_letters used 
    return total_letters

if __name__ == "__main__":
    print(compute())

            
             
