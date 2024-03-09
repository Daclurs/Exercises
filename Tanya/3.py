

strok = int(input('Введите количество строк массива: '))
stolb = int(input('Введите количество столбцов массива: '))
dig = input('Введите числа массива: ')

arr = []
arr1 = []
array = []

for i in range(strok):                  # Создаем новый массив с размером, определенным переменными strok и stolb
    array.append([0] * stolb)
    arr.append([0] * stolb)
    
dig = dig + ' '                         # Проверяем массив, введенный с клавиатуры на наличие чисел
a = ''                                  # и вносим данные в одномерный массив arr1
for x in dig:
    if x.isdigit():
        a = a + x
    else:
        arr1.append(a)
        a = ''
    
ink = 0                                 # Вносим данные из одномерного массива arr1
for i in range(strok):                  # в массив array с размером, определенным переменными strok и stolb
    for j in range(stolb):
        array[i][j] = int(arr1[ink])
        ink = ink + 1

print(array)


def DigSum(num):                        # Функция вычисляет сумму цифр в числе
    z = len(num)
    y = 0
    x = int(num)
    while z > 0:
        q = 10 ** (z - 1)
        v = x // q
        y = y + v
        z = z - 1
        x = x - v * q
    return y
    

for i in range(strok):                  # Записываем числа, сумма цифр, которых четная в массив
    for j in range(stolb):
        if (array[i][j] > 0):
            num = str(array[i][j])
            x = DigSum(num)
            if (x % 2 == 0):
                arr[i][j] = array[i][j]
            else:
                arr[i][j] = '-'

print(arr)