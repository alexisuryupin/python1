new_list = input('заполните список через пробел:').split(' ')
i = 0
print(new_list)
print(type(new_list))
while i + 1 < len(new_list):
    if i % 2 == 0:
        new_list.insert(i, new_list.pop(i + 1))
    i += 1
print(f'Получаем список {new_list}')
