"""4. Написати функцію <prime_list>, яка прийматиме
2 аргументи - початок і кінець діапазона, і вертатиме
список простих чисел всередині цього діапазона. Не забудьте
про перевірку на валідність введених даних
та у випадку невідповідності - виведіть повідомлення."""


def prime_list(first, last):
    if first < last:
        a = []
        for x in range(first, last):
            if x == 2 or x == 3:
                a.append(x)
                continue

            if x % 2 == 0 or x < 2:
                continue

            result = 1
            end = int(x ** .5) + 1
            for i in range(3, end, 2):
                result = x % i
                if not result:
                    break
            if result:
                a.append(x)
        return a
    else:
        return 'Некоректні дані, початкове значення не може бути більше кінцевого'


print(prime_list(0, 100))
