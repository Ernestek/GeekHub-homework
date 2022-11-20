"""2. Створіть за допомогою класів та продемонструйте
свою реалізацію шкільної бібліотеки (включіть фантазію).
Наприклад вона може містити класи Person, Teacher, Student,
Book, Shelf, Author, Category і.т.д. Можна робити по
прикладу банкомату з меню, базою даних і т.д."""
import sqlite3

conn = sqlite3.connect('lib.db')

cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS LIBRARY 
        (ID           PRIMARY KEY        NOT NULL,   
        NAME_BOOK     TEXT UNIQUE        NOT NULL,
        AUTHOR        TEXT               NOT NULL,
        PAGES         INT                NOT NULL,              
        COUNT_BOOK    INT DEFAULT 0);''')
conn.commit()


class Book:
    """
    Класс для ініціалізації книги
    """
    pages_read = 0

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def read_book(self, reading_time, reading_speed):
        try:
            int(reading_time)
        except TypeError:
            print('Некоректне значення')

        if reading_time <= 0 or reading_speed <= 0:
            print('Некоректні значення')
            return
        all_time_reading = self.pages / reading_speed
        if all_time_reading < reading_time:
            print('Ви прочитали книгу швидше запланованого часу')
            self.pages_read = self.pages
            return self.pages_read
        if self.pages_read <= 100:
            pages_read_now = reading_time * reading_speed
            self.pages_read += pages_read_now
            return self.pages_read
        else:
            print('Книга прочитана')

    def book_info(self):
        print(f'Назва: {self.name}, автор: {self.author}, кількість сторінок: {self.pages}')


class Library:
    """
    Класс надає доступ до бібліотеки яка зберігається у lib.db
    """
    _book_in_library = []

    def __load_book(self):
        books = cursor.execute('SELECT NAME_BOOK FROM LIBRARY WHERE COUNT_BOOK > 0').fetchall()
        for book in books:
            self._book_in_library.append(book[0])

    def see_book(self):
        self.__load_book()
        return self._book_in_library

    def take_book(self, name):
        book = cursor.execute('SELECT NAME_BOOK, AUTHOR, PAGES FROM LIBRARY WHERE NAME_BOOK = (?)'
                              'AND COUNT_BOOK > 0', (name,)).fetchone()
        if book:
            cursor.execute('UPDATE LIBRARY SET COUNT_BOOK = COUNT_BOOK - 1 '
                           'WHERE NAME_BOOK = (?)', (name,))
            conn.commit()
            return Book(book[0], book[1], book[2])
        else:
            print("Такої книги нема в бібліотеці")
            return


class Person:
    """
    Батьківський клас для ініціалізації людини
    """
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f'І\'мя: {self.name}, стать: {self.gender}, вік: {self.age}'


class Student(Person):
    my_books = []
    __reading_speed = 0.5

    def __init__(self, name, gender, age, course):
        super().__init__(name, gender, age)
        self.course = course

    def __str__(self):
        return super().__str__() + f', курс: {self.course}'

    def __check_my_books(self, name_book):
        for book in self.my_books:
            if name_book == book.name:
                return book
        print('У тебе нема такої книги')
        return False

    def see_book_info(self, name_book):
        book = self.__check_my_books(name_book)
        if book:
            book.book_info()

    def see_my_books(self):
        print(list([book.name for book in self.my_books]))

    def take_book_in_lib(self, name_book):
        book = Library().take_book(name_book)
        if book is not None:
            self.my_books.append(book)

    def read_book(self, name_book, reading_time):
        if len(self.my_books) <= 0:
            print('У тебе нема книг')
            return
        book = self.__check_my_books(name_book)
        if book:
            book.read_book(reading_time, self.__reading_speed)

    def book_progress(self, name_book):
        book = self.__check_my_books(name_book)
        if book:
            print(f'Прочитано {book.pages_read} зі {book.pages} сторінок книги {book.name}')

    def return_book_to_library(self, name_book):
        book = self.__check_my_books(name_book)
        if book:
            self.my_books.remove(book)
            cursor.execute('UPDATE LIBRARY SET COUNT_BOOK = COUNT_BOOK + 1 WHERE NAME_BOOK = (?)',
                           (name_book,))
            conn.commit()


if __name__ == "__main__":
    std = Student('tom', 'male', 18, 1)
    print(str(std))
    std.take_book_in_lib('The Lord of the Rings1')
    std.take_book_in_lib('The Lord of the Rings')
    std.read_book('The Lord of the Rings', 101)
    std.book_progress('The Lord of the Rings')
    std.take_book_in_lib('Математика')
    std.see_my_books()
    std.see_book_info('Математика')
    std.see_book_info('The Lord of the Rings')
    std.see_book_info('The Lord of the Rings1')
    print('Книги в бібліотеці: ', Library().see_book())
    std.return_book_to_library('Математика')
    std.return_book_to_library('Математика')




