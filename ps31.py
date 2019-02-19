#!/usr/bin/python3 
# England coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
# How many different ways can £2 be made using any number of coins?


# dynamic programming implementation - memoization. 
# memo key: tuple of coins left and amount remaining. value - number of ways 
def totalWays(coinsToConsider, amount, memo = {}):
    # base case - 1 coin to consider
    if len(coinsToConsider) == 1:
        if amount % coinsToConsider[0] == 0:
            return 1 
        else:
            return 0     

    # recursive case 
    coinToUse = coinsToConsider[0]
    n = 0
    ways = 0  
    if amount % coinToUse == 0:
        ways = 1

    while n * coinToUse < amount:
        coinsLeftToConsider = coinsToConsider[1:]
        amountRemaining = amount - n*coinToUse
        try:
            ways += memo[(coinsLeftToConsider, amountRemaining)] 
        except KeyError:
            waysForRemainingCoins = totalWays(coinsLeftToConsider, amountRemaining, memo)
            memo[(coinsLeftToConsider, amountRemaining)] = waysForRemainingCoins
            ways += waysForRemainingCoins
        n += 1    

    return ways 

print(totalWays((1, 2, 5, 10, 20, 50, 100, 200), 200))



# if __name__ == "__main__":
#     possible_coins = [1, 2, 5, 10, 20, 50, 100, 200]
#     print(form_amount(possible_coins, 200))
#     print(len(form_amount(possible_coins, 200)))



