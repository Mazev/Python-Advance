# 1 – Push the element x into the stack.
# 2 – Delete the element present at the top of the stack.
# 3 – Print the maximum element in the stack.
# 4 – Print the minimum element in the stack.

n = int(input())
stacks = []
for i in range(n):
    data = input()
    token = data.split()
    if token[0] == '1':
        number = int(token[1])
        stacks.append(number)
    elif token[0] == '2':
        if stacks:
            stacks.pop()
    elif token[0] == '3':
        print(max(stacks))
    elif token[0] == '4':
        print(min(stacks))


stacks[:] = stacks[::-1]
print(f"{', '.join(str(el) for el in stacks)}")
