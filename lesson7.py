class Product:
    def __init__(self, price):
        self.__price = price  # сделали price приватным атрибутом, теперь его нельзя изменить напрямую

    @property  # создаем геттер для price, чтобы можно было получить его значение
    def price(self):
        return self.__price

    @price.setter  # создаем сеттер для price, чтобы можно было изменить его значение
    def price(self, value):
        if value < 0:
            print("Цена не может быть отрицательной")
        else:
            self.__price = value


p = Product(100)
print(p.price)  # выводим значение price через геттер
p.price = 150  # изменяем значение price через сеттер
print(p.price)  # выводим новое значение price через геттер
p.price = (
    -50
)  # пытаемся установить отрицательное значение price, что вызовет ValueError


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def describe(self):
        return "Круг катится"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def describe(self):
        return "Прямоугольник стоит"


class Square:
    def __init__(self, side):
        self.side = side

    def describe(self):
        return "Квадрат стоит"


for shape in [Circle(5), Rectangle(4, 6), Square(7)]:
    print(f"{shape.describe()}")
