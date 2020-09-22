def lang(arr: list) -> int:
    if not arr:
        return 0
    arr.sort(key=lambda i: i[0])
    dp = [1] * len(arr)
    ans = 1
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i][0] > arr[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
        ans = max(ans, dp[i])
    return ans


if __name__ == "__main__":
    l = [[1, 2], [2, 3], [3, 4]]
    res = lang(l)
    print(res)
