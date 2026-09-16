class Vehicle:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} текущая скорость: {self.speed} км/ч")


class Motorcycle(Vehicle):
    def __init__(self, brand, speed=0, has_sidecar=False):
        super().__init__(brand, speed)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print(
            f"{self.brand} встает на заднее колесо!"
            if not self.has_sidecar
            else "нельзя делать колесо с коляской"
        )


Motorcycle1 = Motorcycle("Harley-Davidson", 100)
Motorcycle2 = Motorcycle("Yamaha", 80, True)
Motorcycle1.accelerate(10)
Motorcycle2.accelerate(20)
Motorcycle1.wheelie()
Motorcycle2.wheelie()
print(isinstance(Motorcycle1, Motorcycle and isinstance(Motorcycle1, Vehicle)))
print(isinstance(Motorcycle2, Motorcycle and isinstance(Motorcycle2, Vehicle)))
