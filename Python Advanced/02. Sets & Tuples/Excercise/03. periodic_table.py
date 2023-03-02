n = int(input())

totals = set()

for el in range(n):
    sequence = input().split()

    for elmnt in sequence:
        totals.add(elmnt)

for x in totals:
    print(x)