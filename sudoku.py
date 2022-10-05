import math


def main(board):
    print(row_col_constraint(board, (1, 7)))


def box_constraint(board, position):
    box_num = position[0]
    cell_num = position[1]
    cell_value = board[box_num][cell_num]
    start_of_box = 0 if cell_num <= 7 else 8
    for i in range(start_of_box, start_of_box + 8):
        if board[box_num][i] == cell_value and i != cell_num:
            return True
    return False


def row_col_constraint(board, position):
    box_num, cell_num = position[0], position[1]
    cell_value = board[box_num][cell_num]
    if box_num == 0:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        row0 = get_row(board, position)
        row1 = get_row(board, (1, row_of_cell*4))
        complete_row = row0 + row1
        if complete_row.count(cell_value) > 1:
            print("true")

        # vertikal
        col_of_cell = get_col_number(cell_num)
        col0 = get_col(board, position)
        col1 = get_row(board, (2, col_of_cell*4))
        complete_col = col0 + col1
        if complete_col.count(cell_value) > 1:
            print("true")

    if box_num == 1:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        row0 = get_row(board, position)
        row1 = get_row(board, (0, row_of_cell * 4))
        complete_row = row0 + row1
        if complete_row.count(cell_value) > 1:
            print("true")

        # vertikal
        col_of_cell = get_col_number(cell_num)
        col0 = get_col(board, position)
        col1 = get_row(board, (3, 0))
        complete_col = col0 + col1
        if complete_col.count(cell_value) > 1:
            print("true")

    return False


def vertical_constraint()


def get_row(board, position):
    row = []
    box_num = position[0]
    cell_num = position[1]
    row_of_cell = math.floor(cell_num / 4)
    start_of_row = row_of_cell * 4
    for i in range(start_of_row, start_of_row + 4):
        row.append(board[box_num][i])
    return row


def get_col(board, position):
    col = []
    box_num = position[0]
    cell_num = position[1]
    col_of_cell = get_col_number(cell_num)
    for i in range(col_of_cell, col_of_cell + 16, 4):
        col.append(board[box_num][i])
    return col


def get_col_number(cell_num):
    # temporary helper
    if cell_num in [0, 4, 8, 12]:
        return 0
    if cell_num in [1, 5, 9, 13]:
        return 1
    if cell_num in [2, 6, 10, 14]:
        return 2
    if cell_num in [3, 7, 11, 15]:
        return 3


if __name__ == "__main__":
    board = [[3, 0, 0, 0,
              0, 2, 0, 0,
              8, 0, 0, 0,
              0, 0, 3, 0],

             [0, 0, 0, 6,
              8, 0, 0, 1,
              7, 0, 0, 0,
              0, 4, 0, 0],

             [0, 0, 0, 0,
              0, 0, 0, 4,
              0, 4, 0, 5,
              3, 0, 0, 0],

             [0, 0, 0, 0,
              0, 0, 5, 0,
              1, 0, 0, 0,
              0, 2, 0, 0],

             [0, 0, 0, 0,
              0, 4, 0, 0,
              0, 2, 0, 6,
              0, 8, 0, 0],

             [0, 2, 0, 8,
              7, 6, 3, 0,
              0, 3, 0, 0,
              0, 0, 0, 6]]
    main(board)
