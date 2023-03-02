def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['X', '!', '@'],
        ]

    else:
        size_square_matrix = int(input())
        matrix = []
        for row_index in range(size_square_matrix):
            row = [' '.join(x) for x in input()]
            matrix.append(row)

        return matrix


def get_symbol(matrix, symbol):
    for row_index in range(len(matrix)):
        for element_index in range(len(matrix[row_index])):

            if matrix[row_index][element_index] == symbol:
                return [True, row_index, element_index]

    return False


def print_result(f_symbol_to_find, f_is_found, f_row=0, f_column=0, ):
    if f_is_found:
        print(f"({f_row}, {f_column})")
    else:
        print(f"{symbol_to_find} does not occur in the matrix")


matrix = read_matrix()
symbol_to_find = input()

result = get_symbol(matrix, symbol_to_find)

if not result:
    print_result(symbol_to_find, result)
else:
    is_found, row, column = result
    print_result(symbol_to_find, is_found, row, column)