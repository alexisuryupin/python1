numbers = [9, 8, 7, 5, 5, 4, 3, 2, 2, 2, 1, ]
user_number = int(input('Введите новый элемент списка:'))
i = 0
for a in numbers:
    if user_number <= a:
        i += 1
numbers.insert(i, user_number)
print(numbers)
