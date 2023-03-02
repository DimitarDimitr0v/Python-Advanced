def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
field = []

total_targets = 0
targets_hit = 0


hit_positions = []
my_position = []


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for field_rows in range(5):
    current_row = input().split()
    field.append(current_row)

    if "A" in field[field_rows]:
        my_position = field_rows, field[field_rows].index('A')

    if 'x' in field[field_rows]:
        total_targets += field[field_rows].count('x')

for _ in range(int(input())):
    command_details = input().split()

    if command_details[0] == "move":
        my_position = move(command_details[1], int(command_details[2]))


    elif command_details[0] == "shoot":
        hit_position = shoot(command_details[1])

        if hit_position:
            hit_positions.append(hit_position)
            targets_hit += 1

        if total_targets == targets_hit:
            print(f"Training completed! All {total_targets} targets hit.")
            break

else:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")

print(*hit_positions, sep='\n')
