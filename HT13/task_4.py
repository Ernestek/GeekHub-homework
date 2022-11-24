"""4. Створіть клас, який буде повністю копіювати
поведінку list, за виключенням того, що індекси в
ньому мають починатися з 1, а індекс 0 має викидати
помилку (такого ж типу, яку кидає list якщо звернутися
до неіснуючого індексу)
"""


# help(list)
class MyList(list):

    def __getitem__(self, index):
        if index == 0:
            raise IndexError("IndexError: list index out of range")
        if index > 0:
            return super(MyList, self).__getitem__(index - 1)
        else:
            return super(MyList, self).__getitem__(index)


q = MyList([3, 4, 5])
print(q)
print(q[-1])
print(q[1])
print(q[0])


