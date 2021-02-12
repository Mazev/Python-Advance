data = input()

symbols = {}
count = 1
for el in data:

    if not el in symbols:
        symbols[el] = [count]
    else:
        symbols[el] += [count]
sortet_dict = dict(sorted(symbols.items(), key=lambda x: x[0]))
for key, value in sortet_dict.items():
    print(f'{key}: {len(value)} time/s')
