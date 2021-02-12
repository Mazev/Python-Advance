n = int(input())

intersections = []

for _ in range(n):
    data = input()
    first_seq_data, second_seg_data = data.split('-')
    start, stop = [int(el) for el in first_seq_data.split(',')]
    firs_seq = range(start, stop + 1)
    start, stop = [int(el) for el in second_seg_data.split(',')]
    second_seg = range(start, stop + 1)
    intersection = set(firs_seq).intersection(second_seg)
    intersections.append(intersection)


longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f'Longest intersection is {list(longest)} with length {len(longest)}')

