"""5. Write a script to remove
values duplicates from dictionary.
Feel free to hardcode your dictionary."""

d = {1: 'bar', 2: 'bar', 3: 'bur', 4: 'bar'}
result = {}

for k, v in d.items():
    if v not in result.values():
        result.update({k: v})

print(result)
