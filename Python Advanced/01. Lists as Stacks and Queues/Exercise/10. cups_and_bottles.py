from collections import deque
cups = input().split()
bottles = input().split()

cups = deque([int(x) for x in cups])
bottles = deque([int(x) for x in bottles])

wasted_water = 0

while len(cups) > 0:
    current_cup = cups[0]

    if len(bottles) > 0:
        current_bottle = bottles[-1]
    else:
        break

    if current_bottle - current_cup >= 0:
        wasted_water += (current_bottle - current_cup)
        cups.popleft()
        bottles.pop()
    else:
        if len(bottles) > 0:
            cups[0] -= current_bottle
            bottles.pop()
        else:
            break

if len(cups) > 0:
    cups_left = []
    for cup in cups:
        cups_left.append(str(cup))
    print(f"Cups: {' '.join(cups_left)}")
    print(f"Wasted litters of water: {wasted_water}")

else:
    bottles_left = []
    for el in bottles:
        bottles_left.append(str(el))

    print(f"Bottles: {' '.join(bottles_left)}")
    print(f"Wasted litters of water: {wasted_water}")