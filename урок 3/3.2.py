def my_func(**kwargs):
    return kwargs


print(my_func(name=input('Введите ваше имя:'), surname=input('Введите вашу фамилию:'),
              data=int(input('Введите год рождения:')), city=input('Ввеедите ваш город:'),
              phone=int(input("Введите ваш номер:")), email=input('Введите ваш email:')))
