def reed_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for row_index in range(rows_count):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def get_column_sum(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])

    sum = []
    for columns_index in range(columns_count):
        column_sum = 0
        for row_index in range(rows_count):
            column_sum += matrix[row_index][columns_index]
        sum.append(column_sum)
    return sum


def print_result(value):
    [print(x) for x in value]


matrix = reed_matrix()
results = get_column_sum(matrix)
print_result(results)
