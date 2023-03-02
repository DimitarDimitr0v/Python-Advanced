rows, columns = list(map(int, input().split()))
snake = input()

index_word = 0
matrix = []

# filling an empty matrix with "0's"
for row in range(rows):
    matrix.append([0 for x in range(columns)])

# filling the matrix with the corresponding element
for row_index in range(rows):
    for col_index in range(columns):
        matrix[row_index][col_index] = snake[index_word]
        index_word += 1
        if index_word == len(snake):
            index_word = 0

# reversing the row every second time
for i in range(len(matrix)):
    if not i == 0 and i % 2 == 1:
        reversed_matrix = matrix[i][::-1]
        print("".join(reversed_matrix))
    else:
        print("".join(matrix[i]))
