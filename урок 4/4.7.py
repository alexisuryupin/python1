from math import factorial


def my_func(num):
    for i in range(1, num + 1):
        yield factorial(i)


n = int(input("Введите число: "))
for el in my_func(n):
    print(el)