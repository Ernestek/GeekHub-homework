"""1. Write a script which accepts a
sequence of comma-separated numbers
from user and generates a list and a
tuple with those numbers."""

numbers = input()

n_list = numbers.split(', ')
n_tuple = tuple(n_list)
print(n_tuple, n_list)



