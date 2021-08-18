from itertools import count, cycle

for i in count(int(input('Введите стратовое число, для выхода из программы нажмите *:'))):
    print(i, end='')
    exit = input()
    if exit == '*':
        break

tekst = input("Введите строку, для выхода нажмите *:")
tekst1 = cycle(tekst)
exit = None

while exit != '*':
    print(next(tekst1), end='')
    exit = input()
    if exit == '*':
        break
