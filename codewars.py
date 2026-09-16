def weight(number):
    weight = 0
    for char in number:
        weight += int(char)
    return weight


def order_weight(strng):
    chek = strng.split()
    chek.sort(key=lambda number: (weight(number), number))
    return " ".join(chek)
