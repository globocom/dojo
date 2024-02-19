def combinations(coins, amount):
    res = []
    for coin in coins:
        while coin <= amount:
            res.append(coin)
            amount -= coin
    if amount == 0:
        return len(res)
    return -1
