def reed_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = reed_matrix()

matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    for i in range(len(row)):
        matrix_sum += row[i]


print(matrix_sum)
print(matrix)

