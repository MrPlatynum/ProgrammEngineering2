def вычислить_факториал(n):
    if n == 0 or n == 1:
        return 1
     else:
        return n * вычислить_факториал(n - 1)
        
n = int(input("Введите число для вычисления факториала: "))
if n < 0:
    print("Факториал отрицательного числа не определен.")