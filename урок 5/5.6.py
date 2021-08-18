with open('tekst6', 'r', encoding='utf-8') as f:
    a = f.readlines(0)
    for i in a:
        new_str = ''.join((i if i in '1234567890' else " ") for i in i)
        new_str2 = [int(i) for i in new_str.split()]
        print(f'{i.split()[0]} {sum(new_str2)}')
