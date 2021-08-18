user_number = int(input('Введеите ваше ввчисло:'))
print(user_number)
number_max = 0
number = user_number
while number > 0:
    number_1 = number_max % 10
    if number_1 > number_max:
        number_max = number_1
        if number_max == 9:
            break
    number = number // 10
    print(f'Самая большая цифра равна {number_max}')