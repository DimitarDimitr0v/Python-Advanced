def read_matrix(row):
    f_matrix = []
    for r in range(row):
        f_matrix.append([int(x) for x in input().split()])

    return f_matrix


rows = int(input())
matrix = read_matrix(rows)
blown = []

bomb_index_pairs = input().split()
bombs = []
expired_bombs_indices = []

for el in bomb_index_pairs:
    bombs.append([int(x) for x in el.split(',')])

for current_bomb in range(0, len(bomb_index_pairs)):
    current_bomb_indices = bomb_index_pairs[current_bomb].split(',')
    r = int(current_bomb_indices[0])
    c = int(current_bomb_indices[1])

    total_bomb_area_coordinates = []
    
    # top_left_diagonal_index
    total_bomb_area_coordinates.append([r - 1, c - 1])
    # top_middle 
    total_bomb_area_coordinates.append([r - 1, c])    
    # top_right_diagonal
    total_bomb_area_coordinates.append([r - 1, c + 1])
    # left_side
    total_bomb_area_coordinates.append([r, c - 1])    
    # right_side
    total_bomb_area_coordinates.append([r, c + 1])
    # bot_left_diagonal
    total_bomb_area_coordinates.append([r + 1, c - 1])    
    # bot_middle
    total_bomb_area_coordinates.append([r + 1, c])
    # bot_right
    total_bomb_area_coordinates.append([r + 1, c + 1])



print(matrix)
