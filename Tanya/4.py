# Вычисление факториала числа при помощи рекурсии

def Rec(n):
    return 1 if n <= 1 else n * Rec(n-1)
    

n = 5
print(Rec(n))


        
