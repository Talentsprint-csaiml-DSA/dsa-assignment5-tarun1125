def min_coins(coins, target_amount):
    dp_array = [target_amount+1 for i in range(target_amount+1)]
    dp_array[0] = 0

    for amount in range(1,target_amount+1):
        for coin in coins:
            if amount - coin >= 0:
                dp_array[amount] = min(dp_array[amount], 1+ dp_array[amount -coin])
    
    return dp_array[target_amount] if dp_array[target_amount] != target_amount + 1 else -1
