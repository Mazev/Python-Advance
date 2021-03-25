from functools import reduce


def operate(operator, *args):
    # result = 0
    # if operator == '+':
    #     for el in args:
    #         result += el
    # elif operator == '-':
    #     for el in args:
    #         result -= el
    # elif operator == '*':
    #     for el in args:
    #         result *= el
    # elif operator == '/':
    #     for el in operator:
    #         result /= el
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
