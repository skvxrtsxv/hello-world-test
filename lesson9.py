from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    color: str
    speed: int = 0

    def accelerate(self, amount):
        self.speed += amount
        print(f"Текущая скорость {self.speed} км/ч")


Car1 = Car("Toyota", "Красный")
Car2 = Car("Toyota", "Красный")

print(Car1 == Car2)
Car2.accelerate(50)
print(Car1 == Car2)
print(Car2)
