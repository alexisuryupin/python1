with open('tekst.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст:')
        if not line:
            break
        print(line, file=f)
        