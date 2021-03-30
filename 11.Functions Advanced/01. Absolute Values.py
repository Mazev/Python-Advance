def convert_iterable_to_absolute(num_list):
    result = [abs(el) for el in num_list]
    return result


num = [float(el) for el in input().split()]

print(convert_iterable_to_absolute(num))