def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4]
        ]

    else:
        (rows_count, columns_count) = map(int, input().split())
        temp_matrix = []
        for row_index in range(rows_count):
            row = list(map(int, input().split()))
            temp_matrix.append(row)
        return temp_matrix


def best_sum_search(matrix, f_rows, f_columns, size):
    summed = 0
    for row in range(f_rows, f_rows + size):
        for col in range(f_columns, f_columns + size):
            current_num = matrix[row][col]
            summed += current_num
    return summed


def get_submatrix_sum(matrix, submatrix_size):
    best_sum = best_sum_search(matrix, 0, 0, submatrix_size)
    best_row_index = 0
    best_column_index = 0

    for row_index in range(len(matrix) - 2):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = best_sum_search(matrix, row_index, col_index, submatrix_size)

            if current_sum > best_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index

    return best_sum, best_row_index, best_column_index


def print_result(coordinates, size):
    (summed, row_index, col_index) = coordinates
    print(f"Sum = {summed}")
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))


matrix = read_matrix()
submatrix_size = 3

print_result(get_submatrix_sum(matrix, submatrix_size), submatrix_size)

