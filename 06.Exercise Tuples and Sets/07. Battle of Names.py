n = int(input())

set_even = set()
set_odd = set()

for counter in range(1, n + 1):
    name = input()
    sum_num = 0
    for el in name:
        sum_num += ord(el)
    result = sum_num // counter
    if result % 2 == 0:
        set_even.add(result)
    else:
        set_odd.add(result)

sum_even = sum(set_even)
sum_odd = sum(set_odd)

if sum_even == sum_odd:
    modified_set = [str(el) for el in set_even.union(set_odd)]
    print(f"{', '.join(modified_set)}")
elif sum_odd > sum_even:
    modified_set = [str(el) for el in set_odd.difference(set_even)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in set_even.symmetric_difference(set_odd)]
    print(f"{', '.join(modified_set)}")
