"""1. Написати функцiю season, яка приймає
один аргумент (номер мiсяця вiд 1 до 12)
та яка буде повертати пору року, до якої
цей мiсяць належить (зима, весна, лiто або осiнь).
У випадку некоректного введеного значення -
виводити відповідне повідомлення."""


def season(num):
    if num in (1, 2, 12):
        return 'зима'
    elif num in (3, 4, 5):
        return 'весна'
    elif num in (6, 7, 8):
        return 'літо'
    elif num in (9, 10, 11):
        return 'осінь'
    else:
        return 'Некоректне значення'


print(season(2))


# Здається дивним, та чомусь мені подобається такий варіант
def season_2(num):
    dict_season = {1: 'зима', 2: 'зима', 3: 'весна',
                   4: 'весна', 5: 'весна', 6: 'літо',
                   7: 'літо', 8: 'літо', 9: 'осінь',
                   10: 'осінь', 11: 'осінь', 12: 'зима'}
    return dict_season.get(num, 'Некоректне значення')


print(season_2(11))
