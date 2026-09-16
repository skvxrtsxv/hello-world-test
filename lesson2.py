# 1
temperature = 23

if temperature > 25:
    print("Жарко")
elif 15 < temperature <= 25:
    print("Комфортно")
else:
    print("Холодно")
# 2
has_umbrella = True
is_raining = False
print("Возьми зонт") if not has_umbrella and is_raining else print("Зонт не нужен")

# 3
age = 25
status = "взрослый" if age >= 18 else "несовершеннолетний"
print(status)
