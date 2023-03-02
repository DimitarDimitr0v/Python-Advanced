def read_matrix(n):
    field = []
    for _ in range(n):
        field.append(input().split())
    return field


def get_tunel_coords(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "T":
                return r, c


size = int(input())
racing_number = input()
car_coords = [0, 0]
initial_kilometers = 0

matrix = read_matrix(size)


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


while True:
    direction = input()

    if direction == "End":
        print(f"Racing car {racing_number} DNF.")
        matrix[car_coords[0]][car_coords[1]] = 'C'
        break

    car_coords[0] += directions[direction][0]
    car_coords[1] += directions[direction][1]

    if matrix[car_coords[0]][car_coords[1]] == "F":
        initial_kilometers += 10
        matrix[car_coords[0]][car_coords[1]] = 'C'
        print(f"Racing car {racing_number} finished the stage!")
        break


    if matrix[car_coords[0]][car_coords[1]] == "T":
        initial_kilometers += 30
        matrix[car_coords[0]][car_coords[1]] = '.'
        tunel_coords = get_tunel_coords(matrix)
        matrix[tunel_coords[0]][tunel_coords[1]] = '.'
        car_coords[0], car_coords[1] = tunel_coords[0], tunel_coords[1]
        continue


    initial_kilometers += 10


print(f"Distance covered {initial_kilometers} km.")

print('\n'.join([''.join(x) for x in matrix]))
