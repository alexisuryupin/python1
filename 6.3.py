class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': profit, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


person = Position('Andrey', 'Smirnov', 'manager', 50000, 10000)
print(person.position)
print(person.get_full_name())
print(person.get_total_income())
print(person.surname)
print(person.name)
