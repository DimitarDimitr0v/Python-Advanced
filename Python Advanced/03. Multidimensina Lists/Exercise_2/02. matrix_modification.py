def index_validation(rows, column, len_matrx):
    if not (0 <= rows <= len(matrix) - 1):
        return False
    elif not (0 <= column <= len(matrix) - 1):
        return False

    return True


matrix_len = int(input())
submatrix = input()
matrix = []


for el in range(matrix_len):

    matrix.append([int(x) for x in submatrix.split()])
    submatrix = input()

command = submatrix

while not command == "END":
    split_command = command.split()
    name = split_command[0]
    row = int(split_command[1])
    col = int(split_command[2])
    value = int(split_command[3])

    if index_validation(row, col, matrix_len):
        if name == 'Add':
            matrix[row][col] += value

        elif name == 'Subtract':
            matrix[row][col] -= value
    else:
        print(f"Invalid coordinates")

    command = input()

for submatrix in matrix:
    for el in submatrix:
        print(el, end=' ')
    print()