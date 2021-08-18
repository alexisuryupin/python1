month = int(input('Введите месяц:'))
winter = {12: 'Декабрь', 1: 'Январь', 2: 'Февраль'}
spring = {3: 'Март', 4: 'Апрель', 5: 'Май'}
summer = {6: 'Июнь', 7: 'Июль', 8: 'Август'}
autumn = {9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь'}

for key in winter:
    if key == month:
        print(f'{month}-й месяц года - это {winter[key]}')
    if month not in winter.keys():
        break
for key in spring:
    if key == month:
        print(f'{month}-й месяц года - это {spring[key]}')
    if month not in spring.keys():
        break

for key in summer:
    if key == month:
        print(f'{month}-й месяц года - это {summer[key]}')
    if month not in summer.keys():
        break
for key in autumn:
    if key == month:
        print(f'{month}-й месяц года - это {autumn[key]}')
    if month not in autumn.keys():
        break

month_dict = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декбрь']
print(f'{month}-й месяц года - это {month_dict[month - 1]}')
