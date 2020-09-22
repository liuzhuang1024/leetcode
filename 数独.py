def slove():
    def dfs(index):
        if index > len(fill)-1:
            return True
        for x in range(1, 10):
            val = str(x)
            if not check(index, val):
                continue
            change(index, val)
            if dfs(index+1):
                return True
            dechange(index)
        return False

    def change(index, val):
        x, y = fill[index]
        board[x][y] = val

    def dechange(index):
        x, y = fill[index]
        board[x][y] = '.'

    def check(index, val):
        x, y = fill[index]
        if val in board[x]:
            return False
        for line in board:
            if val == line[y]:
                return False
        board_x = x // 3 * 3
        board_y = y // 3 * 3
        for i in range(3):
            for j in range(3):
                if val == board[board_x + i][board_y + j]:
                    return False
        return True

    fill = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                fill.append((i, j))

    dfs(0)


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                          "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    slove()
    print(board)
