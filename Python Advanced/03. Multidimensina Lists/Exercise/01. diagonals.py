def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    else:
        matrix = []
        rows = int(input())
        for r in range(rows):
            matrix.append([int(x) for x in input().split(', ')])

        return matrix


def get_primary_diagonal(matrix):
    diagonal_values = []
    for i in range(len(matrix)):
        diagonal_values.append(matrix[i][i])

    return diagonal_values


def get_secondary_diagonal(matrix):
    diagonal_values = []
    index = 0
    for i in range(len(matrix) - 1, -1, -1):
        diagonal_values.append(matrix[i][index])
        index += 1

    return diagonal_values


matrix = read_matrix()

primary_diagonal = get_primary_diagonal(matrix)
secondary_diagonal = (get_secondary_diagonal(matrix)[::-1])

print(f"Primary diagonal: {str(primary_diagonal)[1:-1]}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {str(secondary_diagonal)[1:-1]}. Sum: {sum(secondary_diagonal)}")

