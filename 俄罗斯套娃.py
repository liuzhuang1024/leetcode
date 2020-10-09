

def solve(arr):
    arr.sort()
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i][1] > arr[j][1] and arr[i][0] > arr[j][0]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


if __name__ == "__main__":
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    res = solve(envelopes)
    print(res)
