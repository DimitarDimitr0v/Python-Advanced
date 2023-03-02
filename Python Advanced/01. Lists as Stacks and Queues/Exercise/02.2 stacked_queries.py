n = int(input())

stack = []

for i in range(n):
    query = input().split()

    if query[0] == '1':
        num = int(query[1])
        stack.append(num)

    elif query[0] == '2':
        if len(stack) <= 0:
            pass
        else:
            stack.pop()

    elif query[0] == '3':
        if len(stack) <= 0:
            pass
        else:
            print(max(stack))

    elif query[0] == '4':
        if len(stack) <= 0:
            pass
        else:
            print(min(stack))

print(", ".join(map(str, stack[::-1])))