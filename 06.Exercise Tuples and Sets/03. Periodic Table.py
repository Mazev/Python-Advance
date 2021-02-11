num = int(input())

table = set()

for i in range(num):
    token = input().split()
    for y in token:
        if not y in table:
            table.add(y)

for el in table:
    print(el)