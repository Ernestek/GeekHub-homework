"""4. Write a script which accepts a 
<number> from user and then <number> 
times asks user for string input. 
At the end script must print out result 
of concatenating all <number> strings."""

n = int(input('print number: '))
all_str = []
for _ in range(n):
    all_str.append(input())
print(" ".join(all_str))
