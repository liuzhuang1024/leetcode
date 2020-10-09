def solve(n, k, str1, str2):
    same = 0
    diff = 0
    for i in range(n):
        if str1[i] == str2[i]:
            same += 1
        else:
            diff += 1
    if k == n:
        return [k, k]
    else:
        return [min(abs(n-diff), ), max(same, k)]


if __name__ == "__main__":
    n = 3
    k = 1
    str1 = "ABC"
    str2 = "DDD"
    res = solve(n, k, str1, str2)
    print(res)
