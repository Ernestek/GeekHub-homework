"""2. Створіть 3 рiзних функцiї (на ваш вибiр).
Кожна з цих функцiй повинна повертати якийсь
результат (напр. інпут від юзера, результат
математичної операції тощо). Також створiть
четверту ф-цiю, яка всередині викликає 3 попередні,
обробляє їх результат та також повертає результат
своєї роботи. Таким чином ми будемо викликати одну
(четверту) функцiю, а вона в своєму тiлi - ще 3."""


def print_name(name):
    return name


def print_age(age):
    if age > 18:
        return True
    else:
        print('Sorry, only 18+')
        return False


def print_profession(prof):
    if prof == 'Student':
        return 'please finish your studies'
    else:
        return f'you new {prof}'


def greetings(name, age, prof):
    if print_age(age):
        result = f'Hello {print_name(name)}, {print_profession(prof)}'
        return result
    else:
        return 'See you later'


print(greetings('Tom', 32, 'Student'))
