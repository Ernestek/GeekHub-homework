"""Програма-банкомат."""
import json
import csv
import datetime


def authorization():
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    with open('users.csv', 'r') as file:
        users = csv.DictReader(file)
        state = False
        for row in users:
            if name == row["name"] and password == row['password']:
                state = True
    if state:
        return start(name)
    else:
        print("Ім'я або пароль введено неправильно")


def take_money(name, amount):
    try:
        amount = float(amount)
    except ValueError:
        print('Введено некоректне значення')
        return start(name)

    with open(f'balance/{name}_balance.txt', 'r') as file:
        balance = float(file.read())
        if balance < amount:
            print('Недостатньо коштів')
            print(f'Баланс: {balance}')
            return start(name)
    with open(f'balance/{name}_balance.txt', 'w') as file:
        balance -= round(float(amount), 2)
        print(balance, file=file)
        print(f'Баланс: {balance}')

    with open(f'transactions/{name}_transactions.json', 'a') as file:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
        record = {f'{now}': f'-{amount}'}
        json.dump(record, file)
        file.write('\n')
    return start(name)


def put_money(name, amount):
    try:
        amount = float(amount)
    except ValueError:
        print('Введено некоректне значення')
        return start(name)

    with open(f'balance/{name}_balance.txt', 'r') as file:
        balance = float(file.read())
    with open(f'balance/{name}_balance.txt', 'w') as file:
        balance += round(float(amount), 2)
        print(balance, file=file)
    print(f'Баланс: {balance}')

    with open(f'transactions/{name}_transactions.json', 'a') as file:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
        record = {f'{now}': f'+{amount}'}
        json.dump(record, file)
        file.write('\n')
    return start(name)


def start(name):
    print('1. Баланс\n'
          '2. Поповнити баланс\n'
          '3. Зняти кошти\n'
          '0. Вихід')
    move = input('Введіть цифру: ')
    if move == '1':
        with open(f'balance/{name}_balance.txt', 'r') as file:
            print(file.read())
            return start(name)
    elif move == '2':
        amount = input('Введіть суму: ')
        put_money(name, amount)
    elif move == '3':
        amount = input('Введіть суму: ')
        take_money(name, amount)
    elif move == '0':
        return
    else:
        print('Введено некоректне значення')
        return start(name)


if __name__ == "__main__":
    authorization()
