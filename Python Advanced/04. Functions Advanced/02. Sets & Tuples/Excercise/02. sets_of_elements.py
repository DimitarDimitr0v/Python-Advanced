n = input().split()
sets = [int(x) for x in n]

first_set = set()
second_set = set()

for f in range(sets[0]):
    first_set.add(int(input()))

for s in range(sets[1]):
    second_set.add(int(input()))

result = first_set & second_set

for elmnt in result:
    print(elmnt)