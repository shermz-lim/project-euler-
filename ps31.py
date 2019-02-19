#!/usr/bin/python3 
# England coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p)
# How many different ways can £2 be made using any number of coins?


# dynamic programming implementation - memoization. 
# memo key: tuple of tuple of coins left and amount remaining. value - number of ways to form the amount with remaining coins left 
def totalWays(coinsToConsider, amount, memo = {}):
    """Input: coinsToConsider - tuple of coins that can be used 
        amount - amount that the coins have to form 
        memo - previous solutions to calls of totalWays
        
        returns: no. of ways to form amount with coinsToConsider"""

    # base case - 1 coin to consider
    if len(coinsToConsider) == 1:
        # if remaining 1 coin to consider can form amount, there will be 1 way 
        if amount % coinsToConsider[0] == 0:
            return 1 
        # else there is no way to form the amount  
        else:
            return 0     

    # consider 1st coin in the sequence 
    coinToUse = coinsToConsider[0]
    # n tracks the number of coins to be used 
    n = 0
    ways = 0  
    # the 1 way accounts for when only the coinToUse is used to form the amount 
    # in this case, there will be no coins left to consider. hence, it can't be used 
    # in the recursive case 
    if amount % coinToUse == 0:
        ways = 1

    # recursive case 
    # use 0 to max n - 1 of coinToUse. Then consider no. of ways to form remaining amount with 
    # remaining number of coins 
    while n * coinToUse < amount:
        coinsLeftToConsider = coinsToConsider[1:]
        amountRemaining = amount - n*coinToUse
        try:
            # checks to see whether the solution is in the memo first 
            ways += memo[(coinsLeftToConsider, amountRemaining)] 
        except KeyError:
            # solution not in memo, hence compute it with the recursive case 
            waysForRemainingCoins = totalWays(coinsLeftToConsider, amountRemaining, memo)
            # append solution to memo for future use 
            memo[(coinsLeftToConsider, amountRemaining)] = waysForRemainingCoins
            ways += waysForRemainingCoins
        n += 1    

    # ways will be the no. of ways to form the amount using the coinsToConsider 
    return ways 


if __name__ == "__main__":
    possible_coins = (1, 2, 5, 10, 20, 50, 100, 200)
    print(totalWays(possible_coins, 200))




