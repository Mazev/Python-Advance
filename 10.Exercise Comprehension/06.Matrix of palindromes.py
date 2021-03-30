# rows, cols = [int(el) for el in input().split()]
# result = [[f"{chr(num)}{chr(num2)}{chr(num)}" for num2 in range(num, num + cols)] for num in range(97, 97 + rows)]
# [print(*row) for row in result]
#
# rows, cols = map(int, input().split())
# matrix = [[chr(97+i)+chr(97+i+x)+(chr(97+i)) for x in range(cols)] for i in range(rows)]
# print('\n'.join(" ".join(map(str, el)) for el in matrix))


def read_matrix():
    data = input().split()
    rows = int(data[0])
    columns = int(data[1])
    return [[str(s) for s in range(columns)] for _ in range(rows)]


def get_palindrome_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    first_char_ascii = 97
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = chr(first_char_ascii) + chr(first_char_ascii + c) + chr(first_char_ascii)
        first_char_ascii += 1
    return matrix


def print_result(matrix):
    for r in range(len(matrix)):
        print(" ".join(matrix[r]))


matrix = read_matrix()
palindrome_matrix = get_palindrome_matrix(matrix)
print_result(palindrome_matrix)