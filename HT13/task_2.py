"""
2. Створити клас Matrix, який буде мати наступний функціонал:
1. __init__ - вводиться кількість стовпців і кількість рядків
2. fill() - заповнить створений масив числами - по порядку.
3. print_out() - виведе створений масив (якщо він ще
не заповнений даними - вивести нулі
4. transpose() - перевертає створений масив. Тобто, якщо
взяти попередню таблицю, результат буде
"""

class Matrix:

    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row
        self.data = None

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, column):
        if column < 1:
            raise ValueError('Не може бути менше 1')
        self._column = column

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        if row < 1:
            raise ValueError('Не може бути менше 1')
        self._row = row

    def fill(self):
        k = 0
        len_number = len(str(self.column * self.row)) + 1
        for i in range(self.row):
            arr = []
            for j in range(self.column):
                number = i + k + j + 1
                arr.append(f'{number}'.ljust(len_number))
            k += self.column - 1
            print(''.join(arr))
        self.data = True

    def print_out(self):
        if self.data:
            self.fill()
        else:
            for i in range(self.row):
                arr = []
                for j in range(self.column):
                    arr.append('0'.ljust(2))
                print(''.join(arr))
            self.data = True

    def transpose(self):
        self.column, self.row = self.row, self.column
        self.fill()
        self.column, self.row = self.row, self.column


matrix1 = Matrix(2, 3)
matrix1.print_out()
matrix1.fill()
matrix1.transpose()
matrix1.print_out()
