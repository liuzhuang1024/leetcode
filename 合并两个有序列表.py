def merge(a, b):
    res = []
    while a or b:
        if not a:
            res += b
            break
        elif not b:
            res += a
            break
        if a[0] > b[0]:
            res.append(b.pop(0))
        else:
            res.append(a.pop(0))
    return res


def merge_v2(a, b):
    a_cur = 0

    while b:
        if b[0] >= a[-1]:
            return a+b
        if a[a_cur] > b[0]:
            a.insert(a_cur, b.pop(0))
        a_cur += 1

    return a


if __name__ == "__main__":
    print(merge([1, 2, 4, 6, 78], [34, 55, 77, 88]))
    print(merge_v2([1, 2, 4, 6, 78], [34, 55, 77, 88]))
