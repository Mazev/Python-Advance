# n = int(input())
# stack = []
#
# for i in range(n):
#     line = input().split()
#     command = line[0]
#     if len(line) > 1:
#         element = int(line[1])
#         stack.insert(0, element)
#     elif command == "2":
#         if stack:
#             stack.pop()
#     else:
#         max = 0
#         min = 9999
#         if stack:
#             for el in stack:
#                 if el > max:
#                     max = el
#                 if el < min:
#                     min = el
#             if command == "3":
#                 print(max)
#             elif command == "4":
#                 print(min)
#
# print(f"{', '.join(str(el) for el in stack)}")