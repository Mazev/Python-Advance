def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


number = list(map(int, input().split()))
set_1 = input_to_list(number[0])
set_2 = input_to_list(number[1])

unieque_elements = set(set_1).intersection(set_2)
for i in unieque_elements:
    print(i)