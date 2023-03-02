def get_palindromes(row: int, col: int):
    column_change = 97

    for r in range(97, 97 + row):
        first = chr(r)
        last = chr(r)

        for c in range(column_change, column_change + col ):
            middle = chr(c)

            print(f"{first}{middle}{last}", end=" ")

        print()
        column_change += 1


parameters = input().split()
rows = int(parameters[0])
columns = int(parameters[1])

get_palindromes(rows, columns)