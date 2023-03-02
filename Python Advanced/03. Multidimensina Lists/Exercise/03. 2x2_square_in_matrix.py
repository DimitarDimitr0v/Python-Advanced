def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        (rows_count, columns_count) = list(map(int, input().split()))
        temp_matrix = []
        for row_index in range(rows_count):
            row = input().split()
            temp_matrix.append(row)
        return temp_matrix


def best_sum_search(matrix, f_rows, f_columns, size):
    char_for_comparison = matrix[f_rows][f_columns]
    valid_squares = 0
    for row in range(f_rows, f_rows + size):
        for col in range(f_columns, f_columns + size):
            current_char = matrix[row][col]
            if not current_char == char_for_comparison:
                return False
    else:
        valid_squares += 1

    return valid_squares


def get_submatrix_sum(matrix, submatrix_size):
    valid_squares = 0
    for row_index in range(len(matrix) - 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            valid_squares += best_sum_search(matrix, row_index, col_index, submatrix_size)

    return valid_squares


matrix = read_matrix()
submatrix_size = 2

print(get_submatrix_sum(matrix, submatrix_size))

