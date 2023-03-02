total_numbers = {}

data = input()

while not data.isdigit():
    info = data.split('-')
    name, number = info

    if name not in total_numbers:
        total_numbers[name] = []

    total_numbers[name] = number

    data = input()

people = int(data)

for el in range(people):
    name_for_checking = input()

    if name_for_checking not in total_numbers:
        print(f"Contact {name_for_checking} does not exist.")
    else:
        print(f"{name_for_checking} -> {total_numbers[name_for_checking]}")
        total_numbers.pop(name_for_checking)