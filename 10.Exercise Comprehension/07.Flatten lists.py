input_str = input().split("|")[::-1]

matrix = [x.split() for x in input_str]

flatten_list = [j for i in matrix for j in i]

print(" ".join(flatten_list))