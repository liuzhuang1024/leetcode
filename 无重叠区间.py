def solve(arr: list) -> int:
    if not arr:
        return 0
    arr.sort()
    ans = 1
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i][0] >= arr[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(dp[i], ans)
    return len(arr) - ans
if __name__ == "__main__":
    l = [[1, 2], [1, 2], [1, 2]]
    res = solve(l)
    print(res)
