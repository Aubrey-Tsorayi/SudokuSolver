my_board = [
    [0, 4, 0, 7, 0, 0, 1, 3, 0],
    [0, 0, 2, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 4, 2, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 2, 0, 0, 3],
    [2, 3, 1, 0, 7, 0, 0, 8, 0],
    [4, 0, 0, 3, 1, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 6, 0, 3, 0, 0, 0, 4],
    [8, 9, 0, 0, 5, 0, 0, 0, 6],
]

# checking if the board created is valid
def valid(board, row, col, num):
    # check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # check col
    for i in range(9):
        if board[i][col] == num:
            return False

    # get top-left corner
    c_row = row - row % 3
    c_col = col - col % 3

    # check 3x3 square
    for i in range(c_row, c_row + 3):
        for j in range(c_col, c_col + 3):
            if board[i][j] == num:
                return False

    # return True if none of the cases above returns False
    return True


# function to to check the for zeros and replace with approrite numbers
def solver(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if valid(board, i, j, num):
                        board[i][j] = num
                        result = solver(board)
                        if result:
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True


solver(my_board)

for line in my_board:
    print(line)
