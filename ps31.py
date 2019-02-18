#!/usr/bin/python3 
# England coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
# How many different ways can £2 be made using any number of coins?



def form_amount(possible_coins, amount):
    # base case: if possible coins is an empty list, return an empty set 
    if possible_coins == []:
        return set()
    
    # total ways is an empty set
    total_ways = set()
    # iterate through each coin in possible coins 
    for coin in possible_coins:
        # if amount can be divided equally by coin 
        if amount % coin == 0:
            sequence = (coin,)*(amount//coin)
            print(sequence)
            # total way will include a set formed only by the coin 
            total_ways.add(sequence)

        # recursive case 
        # n tracks the number of the 'coin' that is used 
        remaining_coins = list(possible_coins)
        remaining_coins.remove(coin)

        n = 1 
        while n * coin < amount:
            # amount left after deducting by coin * number used
            remaining_amount = amount - n * coin
            # number of ways to form remaining amount with remaining coins 
            ways_form_remaining = form_amount(remaining_coins, remaining_amount)

            for way in ways_form_remaining:
                sequence = list(way) + [coin]*n
                sequence.sort()
                total_ways.add(tuple(sequence))

            n += 1    

    return total_ways 

print(form_amount([100, 50, 200, 10], 200))    



