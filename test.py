def solve(str1, str2):
    res = ''
    for _ in range(4):
        for i in range(len(str1)):
            for j in range(len(str1[0])):
                if str1[i][j] == '0':
                    res += str2[i][j]

        str2 = list(map(list, zip(*str2[::-1])))
    return res




if __name__ == "__main__":
    str1 = ["1101", "1010", "1111", "1110"]
    str2 = ["ABCD", "EFGH", "IJKL", "MNPQ"]
    str1 = list(map(list, str1))
    str2 = list(map(list, str2))
    res = solve(str1, str2)
    print(res)
