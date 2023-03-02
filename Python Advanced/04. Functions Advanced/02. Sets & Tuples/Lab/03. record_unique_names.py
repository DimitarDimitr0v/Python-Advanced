def arranging(f_n):
    f_names = []
    for _ in range(n):
        current_name = input()

        if current_name not in f_names:
            f_names.append(current_name)

    return f_names


n = int(input())
names = arranging(n)

for x in names:
    print(x)
