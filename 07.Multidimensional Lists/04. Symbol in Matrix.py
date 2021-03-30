def reed_matrix():
    rows_count = int(input())
    matrix = []
    for row_index in range(rows_count):
        row = [x for x in input()]
        matrix.append(row)
    return matrix


def symbol_in_matrix(matrix, symbol):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            curрent_symbol = matrix[row_index][col_index]
            if curрent_symbol == symbol:
                return row_index, col_index


def print_result(result):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = reed_matrix()
symbol = input()
print_result(symbol_in_matrix(matrix, symbol))