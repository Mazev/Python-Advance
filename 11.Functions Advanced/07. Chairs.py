# def combination(names, n, combs=[]):
#     if len(combs) == n:
#         print(", ".join(combs))
#         return
#
#     for i in range(len(names)):
#         name = names[i]
#         combs.append(name)
#         combination(names[i + 1:], n, combs)
#         combs.pop()
#
#
# names = input().split(', ')
# number = int(input())
#
# combination(names, number)
