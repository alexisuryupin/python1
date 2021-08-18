with open('tekst3', 'r', encoding='utf-8') as f:
    my_sum = []
    b = []
    line = f.read().split('\n')
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            b.append(i[0])
        my_sum.append(i[1])

print(f'Зарплата меньше 20000 {b},средняя зарплата составила-{sum(map(float, my_sum)) / len(my_sum)}')
