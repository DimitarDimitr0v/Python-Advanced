def get_matrix(row):
    f_matrix = []
    for r in range(row):
        f_matrix.append([char for char in input()])

    return f_matrix


def get_player_coordinates(f_matrix):
    coordinates = []
    for list_index in range(len(f_matrix)):
        for element_index in range(len(f_matrix[list_index])):
            if f_matrix[list_index][element_index] == 'P':
                coordinates = [list_index, element_index]

    return coordinates


def get_bunny_coordinates(f_matrix):
    bunnies = []
    # list_index = row
    # element_index = column
    for list_index in range(len(f_matrix)):
        for element_index in range(len(f_matrix[list_index])):
            if f_matrix[list_index][element_index] == 'B':
                bunnies.append([list_index, element_index])
    return bunnies


def index_validation(player_position, direction, row_value, col_value):
    direction_indices = {
        'U': (-1, 0),
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0)
    }

    row_offset, col_offset = direction_indices[direction]
    row_current, col_current = player_position

    if direction == 'U' or direction == 'D':
        if -1 <= row_current + row_offset:
            if row_current + row_offset <= row_value:
                return True

        return False

    elif direction == "R" or direction == "L":
        if -1 <= col_current + col_offset:
            if col_current + col_offset <= col_value:
                return True

        return False


def bunny_movement(f_matrix, bunny_positions, row_value, col_value):
    direction_indices = [
        (-1, 0),  # Up
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0)  # Down
    ]

    caught = False
    catch_coordinates = 0

    for current_bunny_coordinates in bunny_positions:
        bunny_row, bunny_col = current_bunny_coordinates

        # loop through all the positions - up, down, left and right
        for current_direction in direction_indices:

            # temp_row and temp_col are the new indices of the - up, down, left or right position
            temp_row = bunny_row + current_direction[0]
            temp_col = bunny_col + current_direction[1]

            # Invalid index check
            if (temp_row == -1 or temp_row > (row_value - 1)) or (temp_col == -1 or temp_col > (col_value - 1)):
                continue

            # Catch check
            if f_matrix[temp_row][temp_col] == 'P':
                f_matrix[temp_row][temp_col] = 'B'
                catch_coordinates = [temp_row, temp_col]
                caught = True
            else:
                f_matrix[temp_row][temp_col] = 'B'

    return f_matrix, catch_coordinates, caught


rows, columns = [int(x) for x in input().split()]
matrix = get_matrix(rows)
directions = input()

is_caught = False
is_finished = False
finish_coordinates = 0
caught_coordinates = 0

for curr_direction in directions:

    direction_mapping = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    # Get the player and bunnies current position indices
    player_row, player_col = get_player_coordinates(matrix)
    bunny_coordinates = get_bunny_coordinates(matrix)

    # Get the row and column indices of the next position based on the current direction
    row_index, col_index = direction_mapping[curr_direction]

    # Calculate the player's new position
    new_row = player_row + row_index
    new_col = player_col + col_index

    # Check if the new position is valid
    if not index_validation((new_row, new_col), curr_direction, rows, columns):
        # player have finished
        matrix[player_row][player_col] = '.'
        matrix, caught_coordinates, is_caught = bunny_movement(matrix, bunny_coordinates, rows, columns)
        finish_coordinates = [player_row, player_col]
        is_finished = True
        break

    # Check if the player has been caught
    if matrix[new_row][new_col] == 'B':
        # player is caught
        matrix[player_row][player_col] = '.'
        matrix, caught_coordinates, is_caught = bunny_movement(matrix, bunny_coordinates, rows, columns)
        caught_coordinates = [new_row, new_col]
        is_caught = True
        break

    # Update the player's position on the matrix
    matrix[player_row][player_col] = '.'
    matrix[new_row][new_col] = 'P'

    # Here we execute the bunny spreading algorithm
    matrix, caught_coordinates, is_caught = bunny_movement(matrix, bunny_coordinates, rows, columns)
    if is_caught:
        break

for x in matrix:
    print(''.join(x))

if is_finished:
    print(f"won: {' '.join(str(x) for x in finish_coordinates)}")

elif is_caught:
    print(f"dead: {' '.join(str(x) for x in caught_coordinates)}")
