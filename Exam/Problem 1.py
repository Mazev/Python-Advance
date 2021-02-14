from collections import deque

firework = deque(input().split(', '))
explosive = deque(input().split(', '))


firework_int = deque([int(el) for el in firework])
explosive_int = deque([int(el) for el in explosive])

palm = {}
willow = {}
crossette = {}

while len(firework_int) > 0:
    if firework_int[0] <= 0:
        firework_int[0].popleft()
    elif explosive_int <= 0:
        explosive_int.pop()
    result = firework_int[0] + explosive_int[0]
    elif result % 3 == 0 and not result % 5 == 0:
        palm[firework_int[0]] = 1
        firework_int.popleft()
        explosive_int.popleft()

    elif result % 3 == 0 and not result % 5 == 0:
        willow[firework_int[0]] = 1
        firework_int.popleft()
        explosive_int.popleft()
    elif result % 3 == 0 and not result % 5 == 0:
        crossette[firework_int[0]] = 1
        firework_int.popleft()
        explosive_int.popleft()
    else:
        firework_int[0] -= 1
        firework_int.popleft()
        firework_int[0].append()


        a = 5
