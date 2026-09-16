from contextlib import contextmanager


def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i


county = 0


def log_call(func):
    def wrapper():
        print(f"Вызов функции {func.__name__}")
        func()
        print("Функция завершена")

    return wrapper


@log_call
def count():
    global county
    county += 1
    print(county)


limit = 10
for number in even_numbers(limit):
    print(number)

count()
count()
count()


@contextmanager
def section(title):
    print(f"===Начало: {title} ===")
    yield
    print(f"===Конец: {title} ===")


with section("Тест"):
    print("код внутри")
