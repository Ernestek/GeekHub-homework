"""7. Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньому і виводить результат.
Елементами списку можуть бути дані будь-яких типів.
    Наприклад:
    1 ,1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ---->
    '1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1'"""


my_list = [1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]]


def element_counter(a):
    array = list(zip(a, map(type, a)))
    new = []
    result = []
    for i in array:
        if i not in new:
            new.append(i)
            result.append(f'{i[0]} -> {array.count(i)}')
    return ', '.join(result)


print(element_counter(my_list))
