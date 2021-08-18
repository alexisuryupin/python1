with open('tekst2', 'r', encoding='utf-8') as f:
    line = f.readlines()
    for index, value in enumerate(line, 1):
        words = len(value.split())
        print(f'Строка под номер {index} содержит {words} слов!')
