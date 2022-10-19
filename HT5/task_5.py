"""5. Написати функцію <fibonacci>, яка приймає один аргумент
і виводить всі числа Фібоначчі, що не перевищують його."""


def fibonacci(n):
    if n == 0:
        print(0)
    elif n > 0:
        a, b = 0, 1
        print(a)
        print(b)
        for i in range(n):
            a, b = b, a + b
            if n >= a:
                print(a)
            else:
                break
    else:
        print("Не існує відємних значень")


fibonacci(0)
