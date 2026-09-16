from collections import Counter
from datetime import datetime
import os
import re

visitors = ["Олег", "Мария", "Олег", "Иван", "Мария", "Олег"]

counts = Counter(visitors)

print(counts.most_common(1))

now = datetime.now()
data = now.strftime("%d-%m-%Y")
print(data)

print(os.path.exists("book.json"))


def extract_numbers(text):
    numbers = re.findall(r"\d+", text)
    return numbers


text1 = "У меня 4 кота и 10 собак и 1 лошадь и 20 куриц и 5 петухов"
result = extract_numbers(text1)
print(result)
