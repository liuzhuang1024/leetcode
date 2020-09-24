def solve(arr: list) -> list:
    def dfs(index):
        if index > len(space) - 1:
            return True
        for char in range(1, 10):
            char = str(char)
            if not check(index, char):
                continue
            i, j = space[index]
            arr[i][j] = char
            if dfs(index + 1):
                return True
            arr[i][j] = '.'

        return False

    def check(index, char) -> bool:
        i, j = space[index]
        if char in arr[i]:
            return False
        for line in arr:
            if char == line[j]:
                return False
        i = i // 3 * 3
        j = j // 3 * 3
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if arr[x][y] == char:
                    return False
        return True
    space = get_space(arr)
    dfs(0)
    i, j = space[-1]
    return arr


def get_space(arr: list) -> list:
    space = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '.':
                space.append((i, j))

    return space


if __name__ == "__main__":
    arr = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
           ["2", ".", ".", ".", ".", ".", ".", ".", "."],
           ["3", ".", ".", ".", ".", ".", ".", ".", "."],
           ["4", ".", ".", ".", ".", ".", ".", ".", "."],
           ["5", ".", ".", ".", ".", ".", ".", ".", "."],
           ["6", ".", ".", ".", ".", ".", ".", ".", "."],
           ["7", ".", ".", ".", ".", ".", ".", ".", "."],
           ["8", ".", ".", ".", ".", ".", ".", ".", "."],
           ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    res = solve(arr)
    print(res)
