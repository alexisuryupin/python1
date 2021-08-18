class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {"налево" if direction == 0 else "направо"}.')

    def car_speed(self):
        return f'{self.speed} - скорость автомобиля. {self.speed} - превышение скорости!' \
            if self.speed > 60 else f'Скорость {self.name} составила - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class Sportcar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class Policecar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(30, 'синей', 'nissan')
town_car.go()
town_car.stop()
print(town_car.car_speed())
town_car.turn(1)
print(f'Машина {town_car.name} -имеет {town_car.color} цвет')

sport_car = Sportcar(100, 'красный', 'bmw')
sport_car.go()
sport_car.stop()
print(sport_car.car_speed())
sport_car.turn(1)
print(f'Машина {sport_car.name} -имеет {sport_car.color} цвет')

work_car = WorkCar(40, 'черный', 'reno')
work_car.go()
work_car.stop()
print(work_car.car_speed())
sport_car.turn(0)
print(f'Машина {work_car.name} -имеет {work_car.color} цвет')

police_car = Policecar(55, 'белый', 'toyota')
police_car.go()
police_car.stop()
print(police_car.car_speed())
police_car.turn(0)
print(f'Машина {police_car.name} -имеет {police_car.color} цвет')
