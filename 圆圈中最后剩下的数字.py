def solve(n, m) -> int:
    arr = list(range(n))
    cur = m - 1 if m < n else m % n - 1
    for i in range(n):
        if len(arr) == 1:
            return arr[-1]
        else:
            arr.pop(cur)
            cur = (cur + m -1) % len(arr) 

    return arr


if __name__ == "__main__":
    n = 10
    m = 17
    res = solve(n, m)
    print(res)
