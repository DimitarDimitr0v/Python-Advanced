def read_matrix(is_test=True):
    if is_test:
        return [
            [11,  2,  4],
            [4,   5,  6],
            [10,  8, -12],
        ]

    else:
        size_square_matrix = int(input())
        matrix = []
        for row_index in range(size_square_matrix):
            row = [int(x) for x in input().split()]
            matrix.append(row)

        return matrix


def get_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]

    return diagonal_sum


def get_second_diagonal_sum(matrix):
    diagonal_sum = 0
    index = 0
    for i in range(len(matrix) - 1, -1, -1):
        diagonal_sum += matrix[i][index]
        index += 1




def print_result(values):
    print(values)


matrix = read_matrix()
result = get_diagonal_sum(matrix)
result_2 = get_second_diagonal_sum(matrix)
print_result(result)
print(result_2)
