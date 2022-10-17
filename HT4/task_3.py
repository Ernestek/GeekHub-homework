"""3. Користувач вводить змінні "x" та "y"
з довільними цифровими значеннями. Створіть
просту умовну конструкцію (звiсно вона
повинна бути в тiлi ф-цiї), під час виконання
якої буде перевірятися рівність змінних "x" та "y"
та у випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y" """


def compare(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Введено некоректне значення")
    else:
        if x > y:
            print(f"х бiльше нiж у на {x - y}")
        elif x < y:
            print(f"у бiльше нiж х на {y - x}")
        else:
            print("х дорівнює y")


num1 = input('Enter number x: ')
num2 = input('Enter number y: ')

compare(num1, num2)
