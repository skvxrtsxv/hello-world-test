def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Деление на ноль невозможно"


print(safe_divide(10, 2))
print(safe_divide(10, 0))


def get_number_from_input(text):
    try:
        return int(text)
    except ValueError:
        return None


print(get_number_from_input("двадцать"))
print(get_number_from_input("20"))
print(get_number_from_input("20.5"))
print(get_number_from_input(34))


class Product:
    def __init__(self, price):
        self.__price = price  # сделали price приватным атрибутом, теперь его нельзя изменить напрямую

    @property  # создаем геттер для price, чтобы можно было получить его значение
    def price(self):
        return self.__price

    @price.setter  # создаем сеттер для price, чтобы можно было изменить его значение
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        else:
            self.__price = value


try:
    p = Product(100)
    print(p.price)  # выводим значение price через геттер
    p.price = 150  # изменяем значение price через сеттер
    print(p.price)  # выводим новое значение price через геттер
    p.price = (
        -50
    )  # пытаемся установить отрицательное значение price, что вызовет ValueError
except ValueError as e:
    print(f"Ошибка: {e}")
finally:
    print(f"Текущее значение: {p.price} Проверка завершена")
