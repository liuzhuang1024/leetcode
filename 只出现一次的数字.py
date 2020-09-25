def solve(arr) -> int:
    tmp = arr[0]
    for i in range(1, len(arr)):
        tmp ^= arr[i]
    return tmp


if __name__ == "__main__":
    arr = [1]
    res = solve(arr)
    print(res)
