class Exceprtion1(Exception):
    def __str__(self):
        return f'На ноль делить нельзя!'
class Del:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dell(self):
        if self.y == 0:
            raise Exceprtion1
        else:
            return self.x/self.y
d = Del(5, 0)
try:
    print(d.dell())
except Exceprtion1 as exeption:
    print("На ноль делить нельзя!")
    