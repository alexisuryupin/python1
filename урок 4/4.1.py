from sys import argv


def salary1():
    try:
        salary, time, bonus = map(int, argv[1:])
        print(f'Заработная плата составит - {salary * time + bonus}')
    except ValueError:
        print('Введите показатели в числах')


salary1()
