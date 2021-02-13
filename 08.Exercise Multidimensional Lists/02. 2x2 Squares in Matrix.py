rows, cols = [int(el) for el in input().split()]


def init_matrix():

    matrix = []
    for _ in range(rows):
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


matrix = init_matrix()

counter = 0
for row_index in range(rows-1):
    for col_index in range(cols-1):
        if chek_elements_equal(row_index, col_index, matrix):
            counter +=1

print(counter)
