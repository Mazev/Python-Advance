data = input()

is_balanced = True
opening = []

maper = {'{':'}', '[':']', '(':')'}
for i in data:
    if i in '{[(':
        opening.append(i)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_i = opening.pop()
        if not maper[current_opening_i] == i:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')