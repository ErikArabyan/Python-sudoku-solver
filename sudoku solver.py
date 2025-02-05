board = [[".", "6", "8", ".", ".", ".", ".", ".", "."],
         ["1", "9", ".", "6", "3", ".", "4", "5", "2"],
         ["3", ".", ".", ".", "5", ".", "7", ".", "6"],
         [".", ".", ".", ".", "1", ".", ".", ".", "3"],
         ["8", "5", ".", ".", "9", "4", "6", "2", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "."],
         ["6", ".", ".", "1", "2", "3", ".", ".", "."],
         ["7", "3", ".", "5", ".", "9", ".", "6", "1"],
         [".", ".", ".", "7", "4", "6", ".", "3", "5"]]

M = 9


def puzzle(board):
    for x in range(9):
        for y in range(9):
            board[x][y] = str(board[x][y])

    for i in range(9):
        print(board[i])


def solve(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True


def Suduko(board, row, col):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == '.':
                board[i][j] = '0'
            board[i][j] = int(board[i][j])

    if row == M - 1 and col == M:
        return True

    if col == M:
        row += 1
        col = 0

    if board[row][col] > 0:
        return Suduko(board, row, col + 1)

    for num in range(1, M + 1, 1):
        if solve(board, row, col, num):
            board[row][col] = num
            if Suduko(board, row, col + 1):
                return True
        board[row][col] = 0

    return False


if (Suduko(board, 0, 0)):
    puzzle(board)
