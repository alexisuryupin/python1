from random import randint

sum_f = 0
with open('tekst5', 'w', encoding='utf-8') as f:
    for i in range(100):
        g = randint(1, 100)
        sum_f += g
        f.write(str(g) + " ")
print(sum_f)
