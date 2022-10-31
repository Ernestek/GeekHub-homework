"""1. Програма-світлофор.
   Створити програму-емулятор світлофора
   для авто і пішоходів. Після запуска програми
   на екран виводиться в лівій половині - колір
   автомобільного, а в правій - пішохідного
   світлофора. Кожну 1 секунду виводиться поточні
   кольори. Через декілька ітерацій - відбувається
   зміна кольорів - логіка така сама як і в звичайних
   світлофорах (пішоходам зелений тільки коли автомобілям червоний)."""
from time import sleep


def traffic_light():
    traffic = ['Green', 'Green', 'Green', 'Green',
               'Yellow', 'Yellow',
               'Red', 'Red', 'Red', 'Red']
    while True:
        for i in traffic:
            yield i


def pedestrian_traffic_light(state):
    if state == 'Green' or state == 'Yellow':
        return 'Red'
    else:
        return 'Green'


if __name__ == '__main__':
    for color in traffic_light():
        print(color.ljust(8) + pedestrian_traffic_light(color).center(10))
        sleep(1)
