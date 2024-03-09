# Ищем сумму цифр в числе

num = input('Введите число: ')

z = len(num)
y = 0
x = int(num)
while z > 0:
    q = 10 ** (z - 1)
    v = x // q
    y = y + v
    z = z - 1
    x = x - v * q
print(y)