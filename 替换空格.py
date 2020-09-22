def slove(s) -> str:
    res = ''
    for i in s:
        if i == ' ':
            res += '%20'
        else:
            res += i
    return res
if __name__ == "__main__":
    s = "We  are  happy."
    res = slove(s)
    print(res)