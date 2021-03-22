# text = input().split()
# print(*[word for word in text if len(word) % 2 == 0], sep='\n')

# data = input().split(', ')
# print(*[f'{word} -> {len(word)}' for word in data], sep=', ')

# country = input().split(', ')
# capitals = input().split(', ')
# print(*[f'{country[index]} -> {capitals[index]}' for index in range(len(country))], sep='\n')


# numbers = [int(el) for el in input().split(', ')]
# print(f"Positive: {', '.join([str(el) for el in numbers if el >= 0])}")
# print(f"Negative: {', '.join([str(el) for el in numbers if el < 0])}")
# print(f"Even: {', '.join([str(el) for el in numbers if el % 2 == 0])}")
# print(f"Odd: {', '.join([str(el) for el in numbers if el % 2 == 1])}")


# n = int(input())
#
# matrix = []
# for i in range(n):
#     row_index = [int(num) for num in input().split(', ')]
#     matrix.append(row_index)
#
# diagonals_1 = []
# diagonals_2 = []
#
# for y in range(len(matrix)):
#     diagonals_1.append(matrix[y][y])
#     diagonals_2.append(matrix[y][n - y - 1])
#
# print(f"First diagonal: {', '.join(str(x) for x in diagonals_1)}. Sum: {sum(diagonals_1)}")
# print(f"Second diagonal: {', '.join(str(x) for x in diagonals_2)}. Sum: {sum(diagonals_2)}")


# r = int(input())
# c = int(input())
#
# matrix = []
# for i in range(r):
#     matrix.append([])
#     for y in range(c):
#         matrix[i].append(0)
#
# print(matrix)
#
# row, cols = [int(el) for el in input().split()]
#
# matrix = [[f"{chr(num)}{chr(nestet_nums)}{chr(num)}"for nestet_nums in range(num, num + cols)] for num in range(97, 97 + row)]
# print(*[' '.join(el) for el in matrix], sep=' \n')

