# 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 2
    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")

    # 3
    def have_birthday(self):
        self.age += 1
        print(f"С днем рождения! Теперь мне {self.age} лет.")


# 4
person1 = Person("Алексей", 30)
person2 = Person("Мария", 25)
person1.introduce()
person2.introduce()
person1.have_birthday()
person1.have_birthday()
person1.introduce()
person2.introduce()
