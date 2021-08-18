from googletrans import Translator

with open('tekst4', 'w', encoding='utf-8') as f:
    with open('tekst44', 'r', encoding='utf-8') as new_f:
        tekst = new_f.read()
    f.write(Translator().translate(tekst, dest='ru').tekst)
