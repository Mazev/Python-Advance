def reed_matrix():
    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def get_even_matrix(matrix):
    return [[x for x in row if x % 2 == 0] for row in matrix]


def print_result(matrix):
    print(even_matrix)


matrix = reed_matrix()
even_matrix = get_even_matrix(matrix)
print_result(matrix)