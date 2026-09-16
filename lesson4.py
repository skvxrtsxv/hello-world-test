# 1
def is_even(number):
    return number % 2 == 0


print(is_even(4))


# 2
def get_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(get_max(5, 10, 3))


# 3
def describe_weather(temperature, is_raining=False):
    if is_raining:
        return "Возьми зонт"
    if temperature > 25:
        return "Жарко"
    elif 15 < temperature <= 25:
        return "Комфортно"
    else:
        return "Холодно"


# 4
print(describe_weather(20))
print(describe_weather(30, True))
print(describe_weather(10, False))
