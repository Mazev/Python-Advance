num = input().split()

stacks = []

for i in range(len(num)):
    stacks.append(num.pop())

print(*stacks)