first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command_split = input().split()

    command_part_one = command_split[0]
    command_part_two = command_split[1]

    values = [int(x) for x in command_split[2::]]

    if command_part_one == "Add":
        if command_part_two == "First":
            first_sequence.update(values)
        elif command_part_two == "Second":
            second_sequence.update(values)

    elif command_part_one == "Remove":
        if command_part_two == "First":
            first_sequence.difference_update(values)
        elif command_part_two == "Second":
            second_sequence.difference_update(values)

    elif command_part_one == "Check":
        if command_part_two == "Subset":
            if first_sequence.issubset(second_sequence):
                print(f"True")
            elif second_sequence.issubset(first_sequence):
                print(f"True")
            else:
                print(f"False")


print(', '.join(str(x) for x in sorted(first_sequence)))
print(', '.join(str(x) for x in sorted(second_sequence)))