def solve(A, B) -> list:
    # 转稀疏矩阵
    # 矩阵乘法i行乘j列
    m, n = len(A), len(B[0])
    A, B = A2B(A), A2B(B)
    res = {}
    for i,j,value_A in A:
        for x,y,value_B in B:
            if j == y:
                if (i,y) in res:
                    res += value_A * value_B
                else:
                    res[(i,y)] = value_A * value_B
    res = [(*key, value) for key,value in res.items()]
    res = B2A(m,n,res)
    return res


def A2B(A) -> list:
    # 转稀疏矩阵
    res = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:
                res.append((i, j, A[i][j]))
    return res


def B2A(m, n, res) -> list:
    # 稀疏转矩阵
    arr = [[0 for i in range(n)] for j in range(m)]
    for i, j, val in res:
        arr[i][j] = val
    return arr


if __name__ == "__main__":
    A, B = [[1, 0, 0], [-1, 0, 5]], [[6, 0, 0], [0, 0, 0], [0, 0, 1]]
    res = solve(A, B)
    print(res)
