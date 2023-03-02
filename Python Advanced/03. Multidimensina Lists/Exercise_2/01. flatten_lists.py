from collections import deque

sequence = input()
modified = sequence.split('|')
split_deque = deque(modified)

matrix_1 = [el.split() for el in deque(sequence.split('|'))]
result = [matrix_1[x] for x in range(len(matrix_1) - 1, -1, -1)]

for submatrix in result:
    for submatrix_el in submatrix:
        print(submatrix_el, end=' ')