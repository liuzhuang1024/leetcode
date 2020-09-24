def solve(arr: list) -> int:
    # 动态规划
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i > 0 and j > 0:
                arr[i][j] += max(arr[i - 1][j], arr[i][j - 1])
            elif i > 0:
                arr[i][j] += arr[i - 1][j]
            elif j > 0:
                arr[i][j] += arr[i][j-1]

    return arr[i][j]


if __name__ == "__main__":
    arr = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    res = solve(arr)
    print(res)
