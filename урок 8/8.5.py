class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = ComplexNumber(7, -5)
c_2 = ComplexNumber(8, 6)
print(c_1 + c_2)
print(c_1 * c_2)
