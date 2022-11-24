"""
1. Створіть клас Car, який буде мати властивість year
рік випуску). Додайте всі необхідні методи до класу,
щоб можна було виконувати порівняння car1 > car2 , яке
буде показувати, що car1 старша за car2. Також, операція
car1 - car2 повинна повернути різницю між роками випуску.
"""
from functools import total_ordering


@total_ordering
class Car:

    def __init__(self, release_year):
        self.release_year = release_year

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, release_year):
        """Перший автомобіль створено 1806"""
        if release_year < 1806:
            raise ValueError('Not a real car')
        self._release_year = release_year

    def __eq__(self, other):
        return self.release_year == other.release_year

    def __lt__(self, other):
        return self.release_year < other.release_year

    def __sub__(self, other):
        return self.release_year - other.release_year


car1 = Car(1992)
car2 = Car(2000)

print(car1 > car2)
print(car1 <= car2)
print(car1 - car2)

car3 = Car(1800)
