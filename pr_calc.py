# Составляем консольный калькулятор
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Деление на ноль невозможно"
    else:
        return x / y


def square(x):
    return x**2


def square_root(x):
    if x < 0:
        return "Невозможно извлечь квадратный корень из отрицательного числа"
    else:
        return x**0.5


def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Квадрат числа")
        print("6. Квадратный корень числа")
        print("7. Выход")

        choice = input("Введите номер операции (1-7): ")
        if choice == "7":
            print("Выход из калькулятора.")
            break
        elif choice in ["5", "6"]:
            x = float(input("Введите число: "))
            if choice == "5":
                print(f"Квадрат: {x}^2 = {square(x)}")
            elif choice == "6":
                print(f"Квадратный корень: √{x} = {square_root(x)}")

        elif choice in ["1", "2", "3", "4"]:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            if choice == "1":
                print(f"Сумма: {x} + {y} = {add(x, y)}")
            elif choice == "2":
                print(f"Разность: {x} - {y} = {subtract(x, y)}")
            elif choice == "3":
                print(f"Произведение: {x} * {y} = {multiply(x, y)}")
            elif choice == "4":
                print(f"Частное: {x} / {y} = {divide(x, y)}")


calculator()
