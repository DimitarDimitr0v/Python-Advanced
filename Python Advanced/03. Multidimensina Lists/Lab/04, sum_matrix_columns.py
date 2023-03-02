def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]

    else:
        (rows_count, columns_count) = map(int, input().split(', '))
        matrix = []
        for row_index in range(rows_count):
            row = [int(x) for x in input().split()]
            matrix.append(row)

        return matrix


def get_column_sums(matrix):
    sums = []
    current_result = 0
    columns = len(matrix[0])
    for column_index in range(columns):
        current_result = 0
        for row_index in range(len(matrix)):
            current_result += matrix[row_index][column_index]
        sums.append(current_result)

    return sums


def print_result(result):
    for el in result:
        print(el)


matrix = read_matrix()
result = get_column_sums(matrix)
print_result(result)
