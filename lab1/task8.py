
n = int(input("Введите натуральное число n (от 1 до 9): "))


if 0 < n < 10:

    for i in range(1, n + 1):
        print(" ".join(["*"] * i))


    for i in range(n - 1, 0, -1):
        print(" ".join(["*"] * i))
else:
    print("Ошибка: число должно быть натуральным и меньше 10.")