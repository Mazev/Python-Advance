from operations import add, divide, multiply, power, subtract


def calculate_expression(expression):
    (x, sing, y) = expression.split(' ')
    x = float(x)
    y = int(y)
    if sing == "/":
        result = x / y
    elif sing == "*":
        result = x * y
    elif sing == "+":
        result = x + y
    elif sing == "-":
        result = x - y
    elif sing == "^":
        result = x ** y
    else:
        raise Exception(f' Invalid sing {sing}')
    return f"{result:.2f}"