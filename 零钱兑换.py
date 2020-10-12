def solve(coins, amount):
    """
    零钱问题I
    注意二者之间的差别
    """
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


def solve_v2(coins, amount):
    """
    零钱问题II
    解析位置   https://leetcode-cn.com/problems/coin-change/solution/yi-bian-jiu-dong-zhi-bei-bao-wen-ti-by-christmas_w/
    """
    if amount == 0:
        return 1
    if amount < 0:
        return -1
    dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(1, len(coins)+1):
        for j in range(1, amount+1):
            if (j - coins[i-1] >= 0):
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i-1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    res = solve_v2(coins, amount)
    print(res)
