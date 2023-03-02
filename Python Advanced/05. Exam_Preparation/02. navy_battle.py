def read_matrix(size):
    field = []
    for row in range(size):
        field.append((' '.join(input())).split())
    return field


def get_submarine_position(field):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "S":
                field[row][col] = "-"
                return row, col


n = int(input())
matrix = read_matrix(n)
submarine_coords = get_submarine_position(matrix)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

submarine_hit_potential = 2
cruisers = 3

while True:
    direction = input()

    curr_row = submarine_coords[0] + directions[direction][0]
    curr_col = submarine_coords[1] + directions[direction][1]

    if matrix[curr_row][curr_col] == "*":
        matrix[curr_row][curr_col] = "-"
        submarine_hit_potential -= 1

        if submarine_hit_potential < 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{curr_row}, {curr_col}]!")
            break


    elif matrix[curr_row][curr_col] == "C":
        matrix[curr_row][curr_col] = "-"
        cruisers -= 1

        if cruisers <= 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    submarine_coords = curr_row, curr_col


matrix[curr_row][curr_col] = "S"
for _ in matrix:
    print("".join(_))

