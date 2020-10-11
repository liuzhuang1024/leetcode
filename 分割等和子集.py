# 继续努力吧
def solve(arr):
    sum_result = sum(arr)
    if sum_result % 2 != 0:
        return False
    sum_result = sum_result // 2
    n = len(arr)
    dp = [[False for j in range(sum_result+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1, n+1):
        for j in range(1, 1+sum_result):
            if j - arr[i-1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[n][sum_result]


if __name__ == "__main__":
    arr = [1, 2, 5]

    res = solve(arr)
    print(res)
