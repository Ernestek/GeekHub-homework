"""9. Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому
проміжку (границі включно). P.S.
Рік є високосним, якщо він кратний 4, але не
кратний 100, а також якщо він кратний 400."""

try:
    start = int(input('Enter start year: '))
    end = int(input('Enter end year: '))
except ValueError:
    print("The entered value is not correct")
else:
    for year in range(start, end+1):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(year)