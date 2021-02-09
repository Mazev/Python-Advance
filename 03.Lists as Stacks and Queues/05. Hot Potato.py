from collections import deque

playears = input().split()
step = int(input())

q = deque(playears)
counter = 0

while len(q) > 1:
    counter += 1
    curent_playears = q.popleft()
    if counter == step:
        print(f'Removed {curent_playears}')
        counter = 0
    else:
        q.append(curent_playears)

print(f'Last is {q.popleft()}')
