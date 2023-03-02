size = int(input())
matrix = [list(input()) for _ in range(size)]

knights_positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2),
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_position = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in knights_positions:
                    new_row, new_col = (row + pos[0]), (col + pos[1])

                    if 0 <= new_row < size and 0 <= new_col < size:

                        if matrix[new_row][new_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks_position = [row, col]

    if knight_with_most_attacks_position:
        r, c = knight_with_most_attacks_position
        matrix[r][c] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)