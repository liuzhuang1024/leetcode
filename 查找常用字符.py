def solve(A: list) -> list:
    if len(A) <= 1:
        return []
    res = []
    tmp = [hash_map(i) for i in A]
    for i in tmp[0].keys():
        Falg = True
        for j in tmp[1:]:
            if i not in j:
                Falg = False
                break
        if Falg:
            res.append(i)
    result = []
    for i in res:
        result += [i for _ in range(min([tmp[x][i] for x in range(len(tmp))]))]
    return result


def hash_map(str_: str) -> dict:
    res = {}
    for char in str_:
        if char not in res:
            res[char] = 1
        else:
            res[char] += 1
    return res


def solve_v2(A: list) -> list:
    """
    改良
    """
    from collections import Counter
    ans = Counter(A[0])
    for str_ in A[1:]:
        ans &= Counter(str_)
    return list(ans.elements())

def solve_v3(A:list)->list:
    from functools import reduce
    from collections import Counter
    return list(reduce(
        lambda x,y:x&y, map(Counter, A)
    ).elements())


if __name__ == "__main__":
    A = ["bella", "label", "roller"]
    res = solve_v3(A)
    print(res)
