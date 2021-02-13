def reed_matrix(matrix):
    (rows_count, columns_count) = map(int, input().split())
    matrix = []
    for row_index in range(rows_count):
        row = [x for x in input().split()]
        matrix.append(row)
    return matrix


def chek_elements_equal(row, col, matr):
    curent_element = matr[row][col]
    next_element_same_row = matr[row][col]
    element_botom = matr[row][col]
    element_botom_right = matr[row + 1][col + 1]
    if curent_element == next_element_same_row and element_botom == element_botom_right:
        return True
    return False


matrix = reed_matrix()
