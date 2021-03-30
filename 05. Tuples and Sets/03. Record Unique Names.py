number = int(input())

names = set()

for i in range(number):
    token = input()
    if not token in names:
        names.add(token)

for person in names:
    print(person)