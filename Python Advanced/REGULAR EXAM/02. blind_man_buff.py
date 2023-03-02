def read_matrix(row):
    field = []
    for el in range(row):
        field.append(input().split())

    return field


def get_player_position(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


rows, cols = [int(x) for x in input().split()]

matrix = read_matrix(rows)
player_coords = get_player_position(matrix)

opponents_caught = 0
moves_made = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

direction = input()

while True:

    if direction == "Finish":
        print("Game over!")
        print(f"Touched opponents: {opponents_caught} Moves made: {moves_made}")
        exit()


    new_row = player_coords[0] + directions[direction][0]
    new_col = player_coords[1] + directions[direction][1]


    if 0 <= new_row < rows and 0 <= new_col < cols:


        if matrix[new_row][new_col] == '-':
            moves_made += 1
            player_coords = new_row, new_col

        elif matrix[new_row][new_col] == "P":
            opponents_caught += 1
            moves_made += 1
            player_coords = new_row, new_col
            matrix[new_row][new_col] = '-'

            if opponents_caught == 3:
                print("Game over!")
                print(f"Touched opponents: {opponents_caught} Moves made: {moves_made}")
                exit()

    direction = input()


