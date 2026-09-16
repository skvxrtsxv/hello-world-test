def get_max(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def find_word(words: list[str], target: str) -> int | None:
    for index, word in enumerate(words):
        if word == target:
            return index
        return None


words = ["кот", "стол", "программирование", "дом", "разработка"]

print(find_word(words, "дом"))
print(find_word(words, "собака"))


def describe_person(name: str, age: int, hobbies: list[str] | None = None) -> str:
    if hobbies is not None:
        return f"{name}, {age} лет. Хобби: {hobbies}"
    else:
        return f"{name}, {age} лет. Хобби не указаны"


person = describe_person("Алексей", 30, ["чтение", "путешествия"])
print(person)
person2 = describe_person("Мария", 25)
print(person2)
