import math


def solve(board):
    find = find_empty_cell(board)
    if not find:
        return board
    else:
        box, cell = find

    for i in range(1, 9):
        if valid_box(board, (box, cell), i) and valid_row_col(board, (box, cell), i):
            board[box][cell] = i

            if solve(board):
                return board
            board[box][cell] = 0
    return False



def valid_box(board, position, cell_value):
    box_num = position[0]
    cell_num = position[1]
    if box_num == 4 or box_num == 5:
        col_of_cell = get_col_number(cell_num)
        col0 = get_col(board, (box_num, col_of_cell))
        col1_start = col_of_cell + 1 if col_of_cell in [0, 2] else col_of_cell - 1
        col1 = get_col(board, (box_num, col1_start))
        complete_col = col0 + col1
        if complete_col.count(cell_value) > 0:
            return False
    else:
        row_of_cell = math.floor(cell_num / 4)
        start_of_row = row_of_cell * 4
        row0 = get_row(board, (box_num, start_of_row))
        row1_start = row_of_cell+1 if row_of_cell in [0, 2] else row_of_cell-1
        row1 = get_row(board, (box_num, row1_start*4))
        complete_row = row0 + row1
        if complete_row.count(cell_value) > 0:
            return False

    return True


def valid_row_col(board, position, cell_value):
    box_num, cell_num = position[0], position[1]
    if box_num == 0:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        if horizontal_constraint(board, position, 1, row_of_cell * 4, cell_value):
            return False

        # vertikal
        col_of_cell = get_col_number(cell_num)
        col0 = get_col(board, position)
        col1 = get_row(board, (2, col_of_cell*4))
        complete_col = col0 + col1
        if complete_col.count(cell_value) > 0:
            return False

    if box_num == 1:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        if horizontal_constraint(board, position, 0, row_of_cell * 4, cell_value):
            return False

        # vertikal
        col_of_cell = get_col_number(cell_num)
        col0 = get_col(board, position)
        col1_start = helper(col_of_cell)
        col1 = get_row(board, (3, col1_start*4))
        complete_col = col0 + col1
        if complete_col.count(cell_value) > 0:
            return False

    if box_num == 2:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        row0 = get_row(board, position)
        row1 = get_col(board, (0, row_of_cell))
        complete_row = row0 + row1
        if complete_row.count(cell_value) > 0:
            return False
        col_of_cell = get_col_number(cell_num)
        if vertical_constraint(board, position, 4, col_of_cell, cell_value):
            return False

    if box_num == 3:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        row0 = get_row(board, position)
        row1_start = helper(row_of_cell)
        row1 = get_col(board, (1, row1_start))
        complete_row = row0 + row1
        if complete_row.count(cell_value) > 0:
            return False
        col_of_cell = get_col_number(cell_num)
        if vertical_constraint(board, position, 5, col_of_cell, cell_value):
            return False

    if box_num == 4:
        # horizontal
        row_of_cell = math.floor(cell_num / 4)
        if horizontal_constraint(board, position, 5, row_of_cell * 4, cell_value):
            return False
        col_of_cell = get_col_number(cell_num)
        if vertical_constraint(board, position, 2, col_of_cell, cell_value):
            return False

    if box_num == 5:
        row_of_cell = math.floor(cell_num / 4)
        if horizontal_constraint(board, position, 4, row_of_cell*4, cell_value):
            return False
        col_of_cell = get_col_number(cell_num)
        if vertical_constraint(board, position, 3, col_of_cell, cell_value):
            return False

    return True


def horizontal_constraint(board, position, box, start_cell, cell_value):
    row0 = get_row(board, position)
    row1 = get_row(board, (box, start_cell))
    complete_row = row0 + row1
    if complete_row.count(cell_value) > 0:
        return True
    return False



def vertical_constraint(board, position, box, start_cell, cell_value):
    col0 = get_col(board, position)
    col1 = get_col(board, (box, start_cell))
    complete_col = col0 + col1
    if complete_col.count(cell_value) > 0:
        return True
    return False


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


def find_empty_cell(board):
    for i, box in enumerate(board):
        for j, cell in enumerate(box):
            if cell == 0:
               return (i, j)
    return None


def helper(num):
    if num == 0:
        return 3
    if num == 1:
        return 2
    if num == 2:
        return 1
    if num == 3:
        return 0


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
    board = [[7, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
             [0, 0, 0, 6, 1, 4, 7, 0, 2, 0, 0, 0, 0, 0, 8, 1],
             [8, 0, 0, 0, 0, 0, 0, 0, 3, 5, 0, 0, 0, 0, 6, 7],
             [0, 0, 0, 0, 0, 0, 0, 4, 5, 0, 7, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 4, 6, 0, 8, 0, 5, 6, 0, 0, 1],
             [0, 2, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 0, 0, 0]]
    solvedBoard = solve(board)
    print(solvedBoard)