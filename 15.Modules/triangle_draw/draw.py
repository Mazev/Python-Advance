def print_tiangle(size):
    for i in range(1, size + 1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        print(' '.join(row))

    for i in range(size - 1, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        print(' '.join(row))



