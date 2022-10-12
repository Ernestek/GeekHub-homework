"""6. Write a script to get the
maximum and minimum VALUE in a dictionary."""

dict_1 = {1: 'aw', 2: 'b', 3: 'bar', 4: 'br'}

try:
    print('max value:', max(dict_1.values()))
    print('min value:', min(dict_1.values()))
except TypeError as err:
    print(err)
