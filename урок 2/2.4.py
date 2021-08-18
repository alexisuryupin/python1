words = input('Введите слова разделенные пробелом:').split()
print(words)
print(type(words))
for i in range(len(words)):
    if len(words[i]) <= 10:
        print(i + 1, words[i])
    else:
        print(i + 1, (words[i])[:10])
