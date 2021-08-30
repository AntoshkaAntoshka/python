class Stationery:
    title = 'Parent'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Рисуем ручкой {self.title}')

class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Рисуем карандашом {self.title}')

class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Рисуем маркером {self.title}')

a = Stationery()
b = Pen()
c = Pencil()
d = Handle()

a.draw() # Запуск отрисовки Parent
b.draw() # Рисуем ручкой Pen
c.draw() # Рисуем карандашом Pencil
d.draw() # Рисуем маркером Handle