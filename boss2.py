def solve(m, n, k) -> int:
    res = n[-1]
    while k != 0:
        if m and n:
            k -= 1
            if m[0] > n[0]:
                res = n.pop(0)
            else:
                res = m.pop(0)

        elif m:
            k -= 1
            res = m.pop(0)
        elif n:
            k -= 1
            res = n.pop(0)
            
    return res


if __name__ == "__main__":
    m, n, k = [1, 2, 2, 7], [3, 4, 5], 5
    res = solve(m, n, k)
    print(res)
