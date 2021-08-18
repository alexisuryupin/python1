while True:
    start_number = int(input("Введите стратовый результат:"))
    finish_number = int(input("Введите финальный результат:"))
    days = 1
    if start_number <= 0 or finish_number <= 0:
        print('Данные введены не верно')
    else:
        while start_number < finish_number:
            start_number += start_number * 0.1
            days += 1
        print(f'Результат будет достигнут на {days} день!')
        break