size = int(input())
matrix = []

collected_tea_bags = 0

for rows in range(size):
    matrix.append(input().split())

    if 'A' in matrix[rows]:
        alice_position = [rows, matrix[rows].index('A')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

matrix[alice_position[0]][alice_position[1]] = '*'

while collected_tea_bags < 10:
    alice_movement = input()

    row = alice_position[0] + directions[alice_movement][0]
    col = alice_position[1] + directions[alice_movement][1]

    if 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == "R":
            matrix[row][col] = "*"
            break

        if matrix[row][col].isdigit():
            collected_tea_bags += int(matrix[row][col])
    else:
        break

    matrix[row][col] = "*"
    alice_position = [row, col]

if collected_tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

for x in matrix:
    print(' '.join(x))