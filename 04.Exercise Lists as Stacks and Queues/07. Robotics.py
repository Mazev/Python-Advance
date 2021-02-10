from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
aveilable_robots = deque()
products = deque()
for el in data:
    robot_data = el.split('-')
    robot = {}
    robot['name'] = robot_data[0]
    robot['procesing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    aveilable_robots.append(robot)

product = input()
while not product == 'End':
    products.append(product)
    product = input()

time = time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()

    if aveilable_robots:
        current_robot = aveilable_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['procesing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time + timedelta(seconds=current_robot['procesing_time'])
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available_at']:
                aveilable_robots.append(r)
        if not aveilable_robots:
            products.append(current_product)
        else:
            current_robot = aveilable_robots.popleft()
            current_robot['available_at'] = time + timedelta(seconds=current_robot['procesing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['procesing_time'])
            print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")

    time = time + timedelta(seconds=1)
