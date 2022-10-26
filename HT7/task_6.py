"""6. Напишіть функцію,яка приймає рядок з
декількох слів і повертає довжину найкоротшого слова.
Реалізуйте обчислення за допомогою генератора в один рядок."""


def min_word(string):
    result = [len(item) for item in string.split(' ') if item]
    return min(result)


print(min_word('hello tom    rwe '))
