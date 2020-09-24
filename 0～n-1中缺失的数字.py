def solve(arr) -> int:
    # 或者二分查找
    for i, j in zip(range(arr[-1]), arr):
        if i != j:
            return i


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    res = solve(arr)
    print(res)
