"""2. Write a script to remove empty elements from a list."""

test = [(), ('hey'), ('',), ('ma', 'ke', 'my'),
        [''], {}, ['d', 'a', 'y'], '', []]

print([value for value in test if value])
