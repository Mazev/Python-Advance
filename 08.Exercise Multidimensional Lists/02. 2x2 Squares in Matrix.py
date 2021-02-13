def reed_matrix():
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = [x for x in input(). split()]
        matrix.append(row)
    return matrix


matrix = reed_matrix()

