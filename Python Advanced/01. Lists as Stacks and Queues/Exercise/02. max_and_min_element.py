queries = int(input())

stack = []

info = input()

for i in range(queries):
    detailed_info = info.split()

    if int(detailed_info[0]) == 1:  # Push
        stack.append(int(detailed_info[1]))

    elif int(detailed_info[0]) == 2:  # Delete
        if len(stack) > 0:
            stack.pop()

    elif int(detailed_info[0]) == 3:  # Print the maximum
        print(max(stack))

    elif int(detailed_info[0]) == 4:  # Print the minimum
        print(min(stack))

    info = input()

final_stack = []

while stack:
    final_stack.append(str(stack.pop()))

print(", ".join(final_stack))