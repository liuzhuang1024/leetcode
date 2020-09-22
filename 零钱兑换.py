def solve(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for j in coins:
            if i - j < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - j])
    return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    res = solve(coins, amount)
    print(res)
