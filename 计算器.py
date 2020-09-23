"""
需要优化
"""


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
    if tmep:
        res.append(int(tmep))
    return res


def list2rpn(arr: list) -> int:
    res = []
    tmp = []
    for char in arr:
        if char == '(':
            tmp.append(char)
        elif char == ')':
            while tmp and tmp[-1] != '(':
                res.append(tmp.pop())
            tmp.pop()
        else:
            if not isinstance(char, int):
                if not tmp:
                    tmp.append(char)
                elif tmp[-1] == '(':
                    tmp.append(char)
                elif char in '-+':
                    if char[-1] in r'*/-+':
                        res.append(tmp.pop())
                        tmp.append(char)
                elif char in '*/':
                    if char[-1] in '*/':
                        res.append(tmp.pop())
                        tmp.append(char)

            else:
                res.append(char)
    while tmp:
        res.append(tmp.pop())
    return res


def rpn(arr: list) -> int:
    nums = []
    res = 0
    while arr:
        char = arr.pop(0)
        if isinstance(char, int):
            nums.append(int(char))
        elif char == '+':
            nums.append(nums.pop() + nums.pop())
        elif char == '-':
            nums.append(nums.pop(-2) - nums.pop())
        elif char == r'/':
            nums.append(nums.pop(-2) / nums.pop())
        elif char == '*':
            nums.append(nums.pop() * nums.pop())
    return nums.pop()


if __name__ == "__main__":
    s = "(1+3)*5*(1-2-3+4+6)+33"
    res = solve(s)
    print(res)
    res = list2rpn(res)
    print(res)
    res = rpn(res)
    print(res)
    print(eval(s))
