"""1. Напишіть програму, де клас «геометричні фігури»
(Figure) містить властивість color з початковим значенням
white і метод для зміни кольору фігури, а його підкласи
«овал» (Oval) і «квадрат» (Square) містять методи _init_
для завдання початкових розмірів об'єктів при їх створенні."""

"""3. Створіть клас в якому буде атрибут який буде рахувати 
кількість створених екземплярів класів.
"""


class InstancesCounter:
    __amount_init = 0

    def __init__(self):
        self.__class__.__amount_init += 1

    @classmethod
    def instances_count(cls):
        return cls.__amount_init


class Figure:
    color = 'white'

    def paint_figure(self, color):
        self.color = color


class Oval(Figure, InstancesCounter):

    def __init__(self, major_axis, minor_axis):
        super().__init__()
        self.major_axis = major_axis
        self.minor_axis = minor_axis


class Square(Figure, InstancesCounter):

    def __init__(self, side):
        super().__init__()
        self.side = side


Square(4)
fig1 = Square(4)
fig1.paint_figure('black')
print(fig1.color)
fig2 = Square(4)
print(fig1.side)
fig6 = Oval(10, 4)
print(fig6.minor_axis, fig6.major_axis)
print('Amount square', Square.instances_count())
print('Amount oval', Oval.instances_count())




