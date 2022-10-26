"""3. Всі ви знаєте таку функцію як <range>.
Напишіть свою реалізацію цієї функції.
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)

   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції -
   можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні
   ситуації (типу range(1, -10, 5) тощо).
   Подивіться як веде себе стандартний range в таких випадках."""


def my_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0
    if type(end) != int or type(start) != int or type(step) != int:
        raise TypeError('input must be an integer')
    if step == 0:
        raise ValueError('arg 3 (step) must not be zero')
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step


for i in my_range(-10, 1, -1):
    print(i)
