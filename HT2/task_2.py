"""2. Write a script which accepts two 
sequences of comma-separated colors 
from user. Then print out a set containing 
all the colors from color_list_1 which are 
not present in color_list_2."""

color_list_1 = set(input().split(', '))
color_list_2 = set(input().split(', '))
print(color_list_1.difference(color_list_2))
