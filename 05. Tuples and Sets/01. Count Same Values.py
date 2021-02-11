number =  tuple(map(float, input().split()))

nums_count = {}
for num in number:
    if not num in nums_count:
        nums_count[num] = 0
    nums_count[num] +=1

for key, value in nums_count.items():
    print(f'{key} - {value} times')


