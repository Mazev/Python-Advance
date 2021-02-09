from collections import deque

n = int(input())

station = deque()

for _ in range(n):
    station.append(input())

petrol_tank = 0

for big_circle in range(n):
    is_valid = True
    for small_circle in range(n):
        current_station = station.popleft()
        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        petrol_tank += petrol

        if petrol_tank >= distance:
            petrol_tank -= distance
            station.append(current_station)
        else:
            is_valid = False
            break
    if is_valid:
        print(big_circle)
        break