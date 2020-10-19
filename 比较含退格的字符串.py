def solve(A: str, B: str) -> bool:
    if A == B:
        return True
    return del_char(A) == del_char(B)


def del_char(A: str) -> str:
    res = []
    A = list(A)
    while A:
        tmp = A.pop(0)
        if tmp != "#":
            res.append(tmp)
        elif res:
            res.pop()
    return res


if __name__ == "__main__":
    S, T = "ab#c",  "#ad#c"
    res = solve(S, T)
    print(res)
