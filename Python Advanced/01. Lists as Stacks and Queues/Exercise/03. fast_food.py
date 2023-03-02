from collections import deque
orders_quantity = int(input())
summed = 0

orders_left = 0
current_orders = [int(x) for x in input().split()]
current_orders_deque = deque(current_orders)

print(max(current_orders))

while current_orders_deque:
    if orders_quantity - summed < current_orders_deque[0]:
        break

    if orders_quantity - int(current_orders_deque[0]) >= 0:
        summed += int(current_orders_deque[0])
        current_orders_deque.popleft()

if len(current_orders_deque) == 0:
    print(f"Orders complete")
else:
    print(f"Orders left:", end=" ")
    for x in current_orders_deque:
        print(x, end=" ")

