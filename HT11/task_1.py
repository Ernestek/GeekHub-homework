"""1. Створити клас Calc, який буде мати атребут
last_result та 4 методи. Методи повинні виконувати
математичні операції з 2-ма числами, а саме додавання,
віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися
до атрибута last_result він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен
повернути результат виконання ПОПЕРЕДНЬОГО методу"""


class Calc:
    """Class used to perform math operations

    ...

    Attributes
    ----------
    result: list
    last_result: int

    Methods
    -------
    addition(num1: int, num2: int):
        return num1 + num2
    subtraction(num1: int, num2: int):
        return num1 - num2
    multiplication(num1: int, num2: int):
        return num1 * num2
    division(num1: int, num2: int):
        return num1 / num2
    """

    result = [None]
    last_result = None

    def addition(self, num1, num2):
        result = num1 + num2
        self.save_last_result(result)
        return result

    def subtraction(self, num1, num2):
        result = num1 - num2
        self.save_last_result(result)
        return result

    def multiplication(self, num1, num2):
        result = num1 * num2
        self.save_last_result(result)
        return result

    def division(self, num1, num2):
        result = num1 / num2
        self.save_last_result(result)
        return result

    def save_last_result(self, result):
        self.last_result = self.result[-1]
        self.result.append(result)
        self.result.pop(0)


op1 = Calc()
print(op1.last_result)
op1.addition(1, 2)
print(op1.last_result)
op1.multiplication(3, 4)
print(op1.last_result)
op1.addition(3, 3)
print(op1.last_result)
