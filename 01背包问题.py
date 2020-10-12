def solve():
    dp = [[0 for i in range(W+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            if j-wt[i-1]<0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i-1]]+val[i-1])
    return dp[N][W]


if __name__ == "__main__":
    N = 3
    W = 5
    wt = [2, 1, 3]
    val = [4, 2, 3]
    res = solve()
    print(res)
