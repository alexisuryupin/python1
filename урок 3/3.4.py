def my_func(x, y):
    try:
        number = x ** y
    except IndentationError:
        return 'expected an indented block '
    return number


print((my_func(4.5, -3)))


def new_func(x1, y1):
    if y1 == 0:
        return 1
    else:
        return ((1 / x1) * new_func(x1, y1 + 1))


x1 = float(input('Введите положительное число:'))
y1 = int(input('Введите целое отрицательное число:'))

print(new_func(x1, y1))
