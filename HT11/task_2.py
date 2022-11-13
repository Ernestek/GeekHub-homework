"""2. Створити клас Person, в якому буде присутнім метод
__init__ який буде приймати якісь аргументи,
які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age,
print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з
екземплярів створіть атрибут profession (його не має
інсувати під час ініціалізації в самому класі) та виведіть
його на екран (прінтоніть)"""


class Person:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def show_age(self):
        return f"{self.age} years old"

    def print_name(self):
        return f"I am {self.name}"

    def show_all_information(self):
        return f"I am {self.name}, me {self.age} years old"


person1 = Person(22, 'Tim')
print(person1.show_all_information())
person1.profession = 'Instructor'
print(person1.profession)

person2 = Person(32, 'Roma')
print(person1.show_all_information())
person1.profession = 'Driver'
print(person1.profession)
