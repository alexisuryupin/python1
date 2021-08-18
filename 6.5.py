class Stationery:
    def __init__(self, title='что то, чем можно рисовать'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Для рисования используйте {self.title} ручку!')


class Pencil(Stationery):
    def draw(self):
        print(f'также можно использовать {self.title} карандаш!')


class Handle(Stationery):
    def draw(self):
        print(f'Или можно попробовать {self.title} маркер!')


a = Stationery()
a.draw()
pen = Pen('шариковую')
pen.draw()
pencil = Pencil("простой")
pencil.draw()
handle = Handle("флюоресцентный")
handle.draw()
