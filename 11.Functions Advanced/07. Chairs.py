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







def combin(names , n , comb =[]):
    if len(comb) == n:
        print(", ".join(comb))
        return
    for i in range(len(names)):
        name = names[i]
        comb.append(name)
        combin(names[i + 1 :], n , comb)
        comb.pop()


names = input().split(', ')
number = int(input())
combin(names, number)







