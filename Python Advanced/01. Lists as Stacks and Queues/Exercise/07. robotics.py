from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(), '%H:%M:%S')
robots = []
available_robots = deque([])

for el in data:
    robot_data = el.split('-')
    robot = {'name': robot_data[0], 'processing_time': int(robot_data[1]), 'available_at': time}
    robots.append(robot)
    available_robots.append(robot)

product = input()
product_line = deque([])

while not product == 'End':
    product_line.append(product)
    product = input()

time = time + timedelta(seconds=1)

while len(product_line) > 0:
    current_product = product_line.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time == r['available_at']:
                available_robots.append(r)

        if not available_robots:
            product_line.append(current_product)

        else:
            current_robot = available_robots.popleft()
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")

    time = time + timedelta(seconds=1)
