import csv

products = [
    {"name": "Product 1", "price": 10.99, "quantity": 5},
    {"name": "Product 2", "price": 5.49, "quantity": 10},
    {"name": "Product 3", "price": 20.0, "quantity": 3},
]

with open("products.csv", "w", newline="") as csvfile:
    fieldnames = ["name", "price", "quantity"]
    writer = csv.DictWriter(
        csvfile, fieldnames=fieldnames
    )  # создаем объект DictWriter, который будет записывать словари в CSV-файл
    writer.writeheader()  # записываем заголовки столбцов в CSV-файл

    for product in products:
        writer.writerow(product)  # записываем каждый словарь в CSV-файл

with open("products.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(
            f"Товар: {row['name']}, Цена: {row['price']}, Количество: {row['quantity']}"
        )
        total_price += float(row["price"]) * float(
            row["quantity"]
        )  # берём из row, а не из products!


def summary():
    with open("products.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        total_price = 0
        for row in reader:
            print(
                f"Товар: {row['name']}, Цена: {row['price']}, Количество: {row['quantity']}"
            )
        total_price += float(row["price"]) * float(
            row["quantity"]
        )  # берём из row, а не из products!


print(f"Общая стоимость всех товаров: {total_price:.2f}")


summary()
