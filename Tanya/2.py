

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
arr = []

def DigSum(num):
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
    

for i in range(len(array)):
    for j in range(len(array[i])):
        if (array[i][j] > 0):
            num = str(array[i][j])
            x = DigSum(num)
            if (x % 2 == 0):
                arr.append(array[i][j])
print(arr)