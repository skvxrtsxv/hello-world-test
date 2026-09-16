# to do list

from datetime import datetime

todo_list = []


def add_task():  # создаем функцию для добавления задачи в список
    task = input("Введите задачу: ")  # запрашиваем у пользователя ввод задачи
    date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )  # получаем текущую дату и время в формате "год-месяц-день часы:минуты:секунды"
    todo_list.append(
        {"task": task, "Дата добавления": date}
    )  # добавляем задачу в список в виде словаря с ключами "task" и "date"


def view_tasks():
    print("Список задач:")
    for index, task in enumerate(
        todo_list
    ):  # проходимся по списку задач и выводим их на экран с индексом
        print(
            f"{index + 1}. {task['task']} (Дата добавления: {task['Дата добавления']})"
        )


def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Выйти")
        choice = input("Выберите действие (1-3): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


menu()
