data = list(input())

stacks = []

for i in range(len(data)):
    stacks.append(data.pop())

print(''.join(stacks))