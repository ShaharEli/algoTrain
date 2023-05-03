# https://leetcode.com/problems/sudoku-solver/

b = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                  ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                return i, j
    return False


def check_if_ok(board, cell, val):
    row, col = cell
    row_diff = row % 3
    col_diff = col % 3
    formatted_row = row - row_diff
    formatted_col = col-col_diff
    for i in range(formatted_row, formatted_row+3):
        for j in range(formatted_col, formatted_col+3):
            if board[i][j] == val:
                return False
    for i in range(len(board)):
        for j in range(len(board)):
            if i == row or j == col:
                if board[i][j] == val:
                    return False
    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for i in range(1, 10):
        if check_if_ok(board, empty_cell, str(i)):
            board[row][col] = str(i)
            if solve_sudoku(board):
                return True
            board[row][col] = "."


solve_sudoku(b)
print(b)
