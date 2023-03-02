from collections import deque
# 91/100

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshake_count = 0
while chocolates and cups_of_milk and milkshake_count < 5:
    chocolate = chocolates[-1]
    milk = cups_of_milk[0]

    if chocolate <= 0:
        chocolates.pop()
    if milk <= 0:
        cups_of_milk.popleft()
    if chocolate <= 0 or milk <= 0:
        continue

    if chocolate == milk:
        milkshake_count += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshake_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print("Chocolate: ", end="")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print("Milk: ", end="")
    print(*cups_of_milk, sep=", ")
else:
    print("Milk: empty")
