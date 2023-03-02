def read_matrix(is_test=False):
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
flattened_matrix = []

for el in matrix:

    for ch in el:
        flattened_matrix.append(ch)

print(flattened_matrix)