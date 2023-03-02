def read_matrix(is_test=True):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
        ]

    else:
        rows_count = int(input())
        matrix = []
        for row_index in range(rows_count):
            row = list(map(int, input().split(', ')))
            matrix.append(row)
        return matrix


matrix = read_matrix()

even_matrix = []
even_matrix_current_index = 0

for el in matrix:
    even_matrix.append([])
    for i in range(len(el)):
        if el[i] % 2 == 0:
            even_matrix[even_matrix_current_index].append(el[i])

    even_matrix_current_index += 1

print(matrix)
print(even_matrix)