"""8. Створити цикл від 0 до ... (вводиться користувачем).
В циклі створити умову, яка буде виводити поточне значення,
якщо остача від ділення на 17 дорівнює 0."""

try:
    num = int(input('Enter number: '))
    for i in range(num + 1):
        if i % 17 == 0:
            print(i)

except ValueError:
    print("The entered value is not a number")
