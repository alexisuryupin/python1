class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        return f'{self._length} м * {self._width} м * 25 кг * 5 см = {(self._length * self._width * 25 * 5)} кг'


road1 = Road(20, 500)
print(road1.massa())
