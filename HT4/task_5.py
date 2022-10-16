"""5. Ну і традиційно - калькулятор :легкая_улыбка:
Повинна бути 1 функцiя, яка приймає 3 аргументи -
один з яких операцiя, яку зробити! Аргументи брати від юзера
(можна по одному - окремо 2, окремо +, окремо 2;
можна всі разом - типу 2 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!"""


def calculator(x, operation, y):
    if x.isdigit() and y.isdigit():
        if operation == '+':
            return x + y
        elif operation == '-':
            return x - y
        elif operation == '*':
            return x * y
        elif operation == '/':
            if y == 0:
                return 'Неможливо поділити на 0'
            else:
                return x / y
        elif operation == '%':
            if y == 0:
                return 'Неможливо поділити на 0'
            else:
                return x % y
        elif operation == '//':
            if y == 0:
                return 'Неможливо поділити на 0'
            else:
                return x // y
        elif operation == '**':
            return x ** y
        else:
            return 'Неможлива операція'
    else:
        return "Некоректні значення"


exam = input('Enter example: ').split()
try:
    print(calculator(exam[0], exam[1], exam[2]))
except IndexError:
    print('Not correct input')
