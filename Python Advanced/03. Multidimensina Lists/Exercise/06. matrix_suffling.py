def get_matrix(row, col):
    f_is_string = False
    init_matrix = []

    for r in range(row):
        current_element = input()

        try:  # Is number
            test = current_element.split()
            int(test[0])
            init_matrix.append([int(x) for x in current_element.split()])

        except ValueError:  # Is String
            f_is_string = True
            current_element = current_element.split()
            for el in current_element:
                init_matrix.append([el])

    return init_matrix, f_is_string


# VALIDATIONS
def swap_and_length_validation(f_command, f_coordinates):
    if not f_command == "swap" or not len(f_coordinates) == 4:
        return False
    return True


def is_num_validation(f_coordinates):
    for el in f_coordinates:
        try:
            int(el)
        except ValueError:
            return False
    return True


def index_validation(f_matrix, f_coordinates, f_is_string):
    row_1 = f_coordinates[0]
    col_1 = f_coordinates[1]
    row_2 = f_coordinates[2]
    col_2 = f_coordinates[3]

    if f_is_string:
        if 0 <= col_1 <= len(f_matrix) - 1:
            if 0 <= col_2 <= len(f_matrix):
                return True
        else:
            return False

    else:
        if 0 <= row_1 <= len(f_matrix) - 1:

            if 0 <= col_1 <= len(f_matrix[row_1]):

                if 0 <= row_2 <= len(f_matrix) - 1:

                    if 0 <= col_2 <= len(f_matrix[row_2]):
                        return True
        else:
            return False


# SHUFFLE
def matrix_shuffle(f_matrix, f_coordinates, f_is_string):
    row_1 = f_coordinates[0]
    col_1 = f_coordinates[1]
    row_2 = f_coordinates[2]
    col_2 = f_coordinates[3]

    if is_string:
        temp = f_matrix[col_1]
        f_matrix[col_1] = f_matrix[col_2]
        f_matrix[col_2] = temp
        return f_matrix

    else:
        temp = f_matrix[row_1][col_1]
        f_matrix[row_1][col_1] = f_matrix[row_2][col_2]
        f_matrix[row_2][col_2] = temp
        return f_matrix


# PRINT RESULT
def print_result(f_matrix, f_is_string):
    if f_is_string:
        for row in f_matrix:
            print(' '.join(str(x) for x in row), end=" ")
        print()
    else:
        for row in f_matrix:
            print(' '.join(str(x) for x in row))


data = [int(x) for x in input().split()]
rows = data[0]
columns = data[1]

extracted_info = get_matrix(rows, columns)
matrix = extracted_info[0]
is_string = extracted_info[1]

info = input()
while not info == "END":
    info_splited = info.split()
    command = info_splited[0]
    coordinates = info_splited[1::]

    if swap_and_length_validation(command, coordinates):
        if is_num_validation(coordinates):
            coordinates = [int(x) for x in info_splited[1::]]
            if index_validation(matrix, coordinates, is_string):
                matrix = matrix_shuffle(matrix, coordinates, is_string)
                print_result(matrix, is_string)

            else:
                print(f"Invalid input!")
        else:
            print(f"Invalid input!")
    else:
        print(f"Invalid input!")

    info = input()
