def read_matrix(size=6):
    data_structure = []
    for row in range(6):
        data_structure.append(input().split())
    return data_structure


def create(row, col, value):
    if matrix[row][col] == ".":
        matrix[row][col] = value
    return row, col


def update(row, col, value):
    if matrix[row][col].isdigit() or matrix[row][col].isalpha():
        matrix[row][col] = value
    return row, col


def delete(row, col):
    if matrix[row][col].isdigit() or matrix[row][col].isalpha():
        matrix[row][col] = '.'
    return row, col


def read(row, col):
    if matrix[row][col].isdigit() or matrix[row][col].isalpha():
        print(matrix[row][col])
    return row, col


matrix = read_matrix()
row_at, col_at = [int(x) for x in input()[1:-1].split(", ")]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


command = input()

while not command == "Stop":
    command_args = command.split(", ")
    name_of_command = command_args[0]
    direction = command_args[1]

    row_offset, col_offset = directions[direction]
    new_row = row_at + row_offset
    new_col = col_at + col_offset

    if name_of_command == "Create":
        value = command_args[2]
        row_at, col_at = create(new_row, new_col, value)

    elif name_of_command == "Update":
        value = command_args[2]
        row_at, col_at = update(new_row, new_col, value)

    elif name_of_command == "Delete":
        row_at, col_at = delete(new_row, new_col)

    elif name_of_command == "Read":
        row_at, col_at = read(new_row, new_col)


    command = input()

for row in matrix:
    print(' '.join(row))