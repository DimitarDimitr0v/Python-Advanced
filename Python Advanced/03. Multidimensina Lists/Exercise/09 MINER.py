def get_matrix(size):
    f_matrix = []
    for rows in range(size):
        f_matrix.append(input().split())
    return f_matrix


def get_miner_coordinates(f_matrix):
    for row in range(len(f_matrix)):
        for col in range(len(f_matrix[row])):
            if f_matrix[row][col] == "s":
                return row, col


def get_total_coal(f_matrix):
    coal = 0
    for row in f_matrix:
        for el in row:
            if el == "c":
                coal += 1
    return coal


def index_validation(size, curr_row, curr_col, off_row, off_col):
    if (miner_row + row_offset > matrix_size - 1) or \
            (miner_col + column_offset > matrix_size - 1) or \
            (miner_row + row_offset < 0) or \
            (miner_col + column_offset < 0):
        return False
    return True


matrix_size = int(input())
directions = input().split()
matrix = get_matrix(matrix_size)

coal_collected = 0
total_coal = get_total_coal(matrix)
new_row = 0
new_column = 0

for current_direction in directions:

    miner_row, miner_col = get_miner_coordinates(matrix)

    direction_indices = {
        'up': (-1, 0),
        'right': (0, 1),
        'left': (0, -1),
        'down': (1, 0)
    }

    row_offset, column_offset = direction_indices[current_direction]
    if not index_validation(matrix_size, miner_row, miner_col, row_offset, column_offset):
        continue
    new_row, new_column = miner_row + row_offset, miner_col + column_offset

    if matrix[new_row][new_column] == 'c':
        matrix[new_row][new_column] = '*'
        coal_collected += 1

    if total_coal <= coal_collected:
        print(f"You collected all coal! ({new_row}, {new_column})")
        break
    if matrix[new_row][new_column] == 'e':
        print(f"Game over! ({new_row}, {new_column})")
        break

    matrix[new_row][new_column] = 's'
    matrix[miner_row][miner_col] = '*'
    miner_row, miner_col = new_row, new_column

else:
    print(f"{total_coal - coal_collected} pieces of coal left. ({new_row}, {new_column})")
