from collections import deque
bullet_price = int(input())
size_of_barrel = int(input())
bullets = input().split()
locks = input().split()
payment = int(input())

bullets = deque([int(x) for x in bullets])
locks = deque([int(x) for x in locks])
current_barrel_size = 0
bullets_shot = 0

while len(locks) > 0:

    if len(bullets) > 0:
        current_bullet = bullets.pop()

        if current_bullet > locks[0]:
            print(f"Ping!")
            current_barrel_size += 1
            bullets_shot += 1
            if len(bullets) <= 0:
                break
            elif current_barrel_size >= size_of_barrel:
                current_barrel_size = 0
                print(f"Reloading!")
        else:
            locks.popleft()
            print(f"Bang!")
            current_barrel_size += 1
            bullets_shot += 1
            if len(bullets) <= 0:
                break
            elif current_barrel_size >= size_of_barrel:
                current_barrel_size = 0
                print(f"Reloading!")
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        exit()


money_left = payment - (bullets_shot * bullet_price)

if len(locks) <= 0:
    print(f"{len(bullets)} bullets left. Earned ${money_left}")

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")