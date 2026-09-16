class Car:
    total_cars = 0

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0
        Car.total_cars += 1  # увеличиваем счетчик при создании нового объекта Car

    def accelerate(self, amount):
        self.speed += amount
        print(f"Текущая скорость {self.speed} км/ч")

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars  # возвращаем общее количество созданных объектов Car

    @staticmethod
    def is_valid_speed(speed):
        if speed >= 0:
            return True
        else:
            return False


Car1 = Car("Toyota", "Красный")
Car2 = Car("Honda", "Синий")
Car3 = Car("Ford", "Черный")

print(
    Car.get_total_cars()
)  # вызовем метод класса для получения общего количества созданных объектов Car
print(Car.is_valid_speed(50))  # вызовем статический метод для проверки скорости
print(Car.is_valid_speed(-10))  # вызовем статический метод для проверки скорости
