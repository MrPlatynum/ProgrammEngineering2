def вычислить_факториал(n):
    if n == 0 or n == 1:
        return 1
     else:
        return n * вычислить_факториал(n - 1)