def reed_matrix():
    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def left_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def rath_diagonal(matrix):
    col = len(matrix) - 1
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][col]
        col -= 1
    return diagonal_sum


matrix = reed_matrix()
difrens = abs(left_diagonal(matrix) - rath_diagonal(matrix))

print(difrens)