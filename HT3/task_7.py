"""7. Write a script which accepts a <number>(int)
from user and generates dictionary in range <number>
where key is <number> and value is <number>*<number>"""

try:
    num = int(input('Enter number: '))
except ValueError:
    print("The entered value is not a number")
else:
    dict_num = dict()
    for key in range(num + 1):
        dict_num.update({key: key * key})
    print(dict_num)
