"""1. Write a script that will run through
a list of tuples and replace the last value
for each tuple. The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different."""

value = input("Enter value: ")
list_tuple = [(1, 2), (1, 2, 3), ()]
new = []

for i in list_tuple:
    if not i:
        new.append(i)
    else:
        i = i[:-1] + (value,)
        new.append(i)

print(new)
