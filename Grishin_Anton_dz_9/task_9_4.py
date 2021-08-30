class Car:
    # Базовый класс автомобиля
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def go(self):
        print(f'{self.color} {self.name} поехала')

    def stop(self):
        print(f'{self.color} {self.name} поехала')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.color} {self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')

class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self): # проводим переопределение
        print(f'Скорость: {self.speed}') if self.speed <= int(60) else print('Превышена максимальная скорость')

class SportCar(Car):
    pass

class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        print(f'Скорость: {self.speed}') if self.speed <= int(40) else print('Превышена максимальная скорость')

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)

c = Car(40, 'white', 'audi')
t = TownCar('bmw', 'black', 70)
s = SportCar(40, 'red', 'ferrari')
w = WorkCar(40, 'purple', 'lada')
p = PoliceCar(40, 'grey', 'skoda')

t.go() # black bmw поехала
t.turn('налево') # black bmw повернула налево
t.stop() # black bmw поехала
t.show_speed() # Превышена максимальная скорость
