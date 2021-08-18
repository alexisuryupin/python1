number_1 = float(input('Введите выручку фирмы:'))
number_2 = float(input('Введите издержки фирмы:'))
result = number_1 - number_2
if result > 0:
    print(f'Прибыль фирмы составила {result} рублей!')
    person = int(input('Введите кол-во сотруднкиов:'))
    print(f'Прибыль на каждого сотрудника составит {result / person} рублей!')
elif result < 0:
    print(f'Ваша фирма потеряла {result} рублей!')
else:
    print('Ваша фирма не смогла заработать, но и не потеряла ни рубля!')