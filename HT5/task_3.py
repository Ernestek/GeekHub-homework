"""3. Написати функцию <is_prime>, яка прийматиме 
1 аргумент - число від 0 до 1000, и яка вертатиме 
True, якщо це число просте і False - якщо ні."""


def is_prime(x):
    if x == 2 or x == 3:
        return True

    if x % 2 == 0 or x < 2:
        return False

    end = int(x ** .5 + 1)
    for i in range(3, end, 2):
        if x % i == 0:
            return False
    return True

print(is_prime(-1))


