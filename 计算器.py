def solve(s: str) -> int:
    # 实现不带括号的计算器
    s = list(s)
    res = []
    tmep = ''
    while s:
        tmp = s.pop(0)
        if tmp in r'+-()*/':
            if tmep != '':
                res.append(int(tmep))
                tmep = ''
            res.append(tmp)
        else:
            tmep += tmp
    return res


def list2rpn(arr: list) -> int:
    pass



if __name__ == "__main__":
    s = '1333+3222+3*(1+2-3)'
    res = solve(s)
    print(res)
    res = list2rpn(res)
    print(res)
