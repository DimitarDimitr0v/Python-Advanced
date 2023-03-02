players = input().split()  # [George, Peter, Michael, William, Thomas]
jump_over = int(input())  # 10
i = 0

while players:
    if len(players) == 1:
        print(f"Last is {players[0]}")
        break

    if not i == jump_over - 1:
        players.append(players[0])
        players.pop(0)
        i += 1
    else:
        print(f"Removed {players[0]}")
        players.pop(0)
        i = 0



