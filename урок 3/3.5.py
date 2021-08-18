def my_func():
    num = 0
    while True:
        numbers = input("Введите числа через пробел, для выхода нажмите *:")
        for i in numbers:
            if i == '*':
                return num
            else:
                try:
                    num += int(i)
                except ValueError:
                    print("Чтобы выйти из программы нажмите *")
        print(f'Сумма = {num}')


print(my_func())
