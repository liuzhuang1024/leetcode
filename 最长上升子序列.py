def solve(arr):
    dp = [1] * len(arr)
    ans = 1
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(dp[i], ans)
    return ans

if __name__ == "__main__":
    l = [10, 9, 2, 5, 3, 7, 101, 18]
    res = solve(l)
    print(res)
