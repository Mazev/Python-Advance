def reed_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    matrix = []
    for row_index in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def get_sum_of_submatrix(matrix, row_index, col_index, size):
    the_sum = 0
    for i in range(row_index, row_index + size):
        for c in range(col_index, col_index + size):
            the_sum += matrix[i][c]
    return the_sum

def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
    best_row_index = 0
    best_col_index = 0
    best_sum = get_sum_of_submatrix(matrix, best_row_index, best_col_index, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_col_index = col_index
    return best_row_index, best_col_index


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_of_submatrix(matrix, row_index, col_index, size))


submatrix_size = 2
matrix = reed_matrix()
coordinates = get_best_submatrix_sum_coordinates(matrix, submatrix_size)
print_result(coordinates, submatrix_size)