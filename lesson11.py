import json

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка \nВторая строка \nТретья строка")

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

book = {
    "title": "Python для начинающих",
    "author": "Иван Иванов",
    "year": 2023,
    "is_read": True,
}
with open("book.json", "w", encoding="utf-8") as file:
    json.dump(book, file, ensure_ascii=False, indent=4)

with open("book.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(data.get("title"), data.get("author"))
