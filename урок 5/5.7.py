import json

with open('tekst77.json', 'w', encoding='utf-8') as f:
    with open('tekst7', encoding='utf-8') as f1:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f1}
        result = [profit, {'new_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, f, ensure_ascii=False, indent=4)
