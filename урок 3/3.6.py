def int_func(words):
    for i in words:
        if i.isupper():
            print("Вы ввели слова с большой буквы!")
            words = input('Введите слова с маленькой буквы:')
            break

    word_list =words.split()
    for i in range(len(word_list)):
        print(word_list[i][0].upper() + word_list[i][1:], end=" ")

int_func(input('Введеите слова с маленьких латинских букв:'))
