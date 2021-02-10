from collections import deque

n = int(input())

station = deque([])

for _ in range(n):
    station.append([el for el in input().split()])


for big_circle in range(n):
    is_valid = True
    petrol_tank = 0
    for small_circle in range(n):
        petrol_tank += int(station[small_circle][0]) - int(station[small_circle][1])

        if petrol_tank < 0:
            is_valid = False
            station.append(station.popleft())
            break
    if is_valid:
        print(big_circle)
        break
