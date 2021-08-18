number1 = int(input('Введите первое число:'))
number2 = int(input('Введите второе число:'))


def my_func(number1, number2):
    if number1 == 0 or number2 == 0:
        print('Err!')
    else:
        return number1 / number2


print(my_func(number1, number2))






