def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


num = int(input())
result = input_to_list(num)
result = set(result)
for i in result:
    print(i)

