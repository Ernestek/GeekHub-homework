"""Програма-банкомат.
admin/admin
ernest/qwerty1
roman/roma12"""
import datetime
import sqlite3

conn = sqlite3.connect('bank.db')

cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS USERS 
        (ID           PRIMARY KEY        NOT NULL,   
        NAME          TEXT UNIQUE        NOT NULL,
        PASSWORD      TEXT               NOT NULL,
        BALANCE       INT DEFAULT 0,
        TRANSACTIONS  TEXT DEFAULT "");''')
conn.commit()

conn.execute('''CREATE TABLE IF NOT EXISTS ATM
        (ID     PRIMARY KEY      NOT NULL,
        NAME         TEXT        NOT NULL,
        AMOUNT       INT DEFAULT 0);''')
conn.commit()


def validation_password(password):
    if len(password) < 6:
        print('the password is too short (min 6 char)')
        return False
    elif not any(map(str.isdigit, password)):
        print('password must have at least one digit')
        return False
    elif not any(map(str.isalpha, password)):
        print('password must have at least one alpha')
        return False
    elif any(map(str.isspace, password)):
        print('password must not have spaces')
        return False
    return True


def validation_name(name):
    if len(name) < 3 or len(name) > 51:
        print('name length should be >4 and <51')
        return False
    return True


def registration():
    name = input('0. Exit\n'
                 'Come up with a name: ')
    if name == '0':
        return input_menu()

    cursor.execute("SELECT id FROM USERS ORDER BY id DESC ")
    id_sel = cursor.fetchone()[0] + 1

    list_users = cursor.execute("SELECT NAME FROM USERS").fetchall()
    for user in list_users:
        if name == user[0]:
            print('This name is already used')
            return registration()
        if not validation_name(name):
            return registration()
    for _ in range(10):
        password = input('Come up with a password: ')
        if not validation_password(password):
            continue
        cursor.execute("INSERT INTO USERS (id,NAME,PASSWORD) VALUES ((?), (?), (?))", (id_sel, name, password))
        conn.commit()
        print(f'Вітання, {name}, ')
        return start(name)
    print('Невдала спроба')
    return input_menu()


def authorization():
    name = input('Введіть логін: ')
    password = input('Введіть пароль: ')
    state = False

    if name == 'admin' and password == 'admin':
        return admin_menu(name)

    list_name = cursor.execute("SELECT NAME, PASSWORD FROM USERS").fetchall()

    for user in list_name:
        if name == user[0] and password == user[1]:
            state = True
    if state:
        return start(name)
    else:
        print("Ім'я або пароль введено неправильно")
        return input_menu()


def balance(name):
    money = cursor.execute("SELECT BALANCE FROM USERS WHERE NAME=(?)", (name,)).fetchone()
    return money[0]


def take_money(name, amount):
    try:
        amount = float(amount)
    except ValueError:
        print('Введено некоректне значення')
        return start(name)

    if amount < 0:
        print('Некоректне значення')
        return start(name)

    my_balance = balance(name)
    if my_balance < amount:
        print('Недостатньо коштів')
        print(f'Баланс: {my_balance}')
        return start(name)

    if atm_balance() < amount:
        print('Недостатньо коштів в банкоматі\n'
              f'Максимальна сума зняття: {atm_balance()}')
        return start(name)

    change = amount % 10
    amount -= change
    print(f'Знято {int(amount)}')
    cursor.execute("UPDATE USERS SET balance = balance - (?) WHERE NAME = (?)",
                   (amount, name))

    print(f'Баланс: {balance(name)}')

    now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
    record = {f'{now}: -{amount}\n'}
    cursor.execute("UPDATE USERS SET TRANSACTIONS = TRANSACTIONS || (?) WHERE NAME = (?)",
                   (str(record), name))
    conn.commit()
    return start(name)


def put_money(name, amount):
    try:
        amount = int(amount)
    except ValueError:
        print('Введено некоректне значення')
        return start(name)

    if amount < 0:
        print('Некоректне значення')
        return start(name)

    change = amount % 10
    amount -= change
    cursor.execute("UPDATE USERS SET balance = balance + (?) WHERE NAME = (?)",
                   (int(amount), name))
    print(f'Внесено: {amount}\n'
          f'Баланс: {balance(name)}\n'
          f'Решта: {change}')

    now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
    record = {f'{now}: +{amount}\n'}
    cursor.execute("UPDATE USERS SET TRANSACTIONS = TRANSACTIONS || (?) WHERE NAME = (?)",
                   (str(record), name))
    conn.commit()

    return start(name)


def atm_balance():
    bills = cursor.execute("SELECT name, amount FROM ATM").fetchall()
    result = 0
    for i in bills:
        result += int(i[0]) * i[1]
    return result


def take_bill_admin():
    num = ('10', '20', '50', '100', '200', '500', '1000')
    bill = input('0. Назад\n'
                 'Введіть номінал: ')
    if bill == '0':
        return admin_menu('admin')
    if bill not in num:
        print('Невідома купюра')
        return take_bill_admin()
    try:
        amount = int(input('Введіть кількість: '))
    except ValueError:
        print('Некоректні дані')
        return take_bill_admin()
    else:
        if amount < 0:
            print('Некоректні дані')
            return take_bill_admin()
        bank_amount_bill = cursor.execute("SELECT amount FROM ATM WHERE name = (?)", (bill,)).fetchone()
        if amount > bank_amount_bill[0]:
            print(f'Недостатньо купюр, наявна кількість: {bank_amount_bill[0]}')
            return take_bill_admin()
        cursor.execute("UPDATE ATM SET amount = amount - (?) WHERE name = (?)",
                       (amount, bill))
        now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
        record = f'{now} вилучено {amount} купюр, номиналом {bill}\n'
        cursor.execute("UPDATE USERS SET TRANSACTIONS = TRANSACTIONS || (?) WHERE NAME = (?)",
                       (record, 'admin'))
        conn.commit()
    return admin_menu('admin')


def put_bill_admin():
    num = ('10', '20', '50', '100', '200', '500', '1000')
    bill = input('0. Назад\n'
                 'Введіть номінал: ')
    if bill == '0':
        return admin_menu('admin')
    if bill not in num:
        print('Невідома купюра')
        return put_bill_admin()
    try:
        amount = int(input('Введіть кількість: '))
    except ValueError:
        print('Некоректні дані')
        return put_bill_admin()
    else:
        if amount < 0:
            print('Некоректні дані')
            return put_bill_admin()

        cursor.execute("UPDATE ATM SET amount = amount + (?) WHERE name = (?)",
                       (amount, bill))
        now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
        record = f'{now} внесено {amount} купюр, номиналом {bill}\n'
        cursor.execute("UPDATE USERS SET TRANSACTIONS = TRANSACTIONS || (?) WHERE NAME = (?)",
                       (record, 'admin'))
        conn.commit()
    return admin_menu('admin')


def input_menu():
    move = input('1. Авторизація\n'
                 '2. Реєстрація\n'
                 '0. Вихід\n'
                 'Введіть цифру: ')
    if move == '1':
        authorization()
    elif move == '2':
        registration()
    elif move == '0':
        return
    else:
        print('Введено некоректне значення')
        return input_menu()


def admin_menu(name):
    print('1. Баланс банкомату\n'
          '2. Кількість купюр\n'
          '3. Внести купюри\n'
          '4. Вилучити купюри\n'
          '0. Вихід')
    move = input('Введіть цифру: ')
    if move == '1':
        print(atm_balance())
        return admin_menu(name)
    elif move == '2':
        bills = cursor.execute("SELECT name, amount FROM ATM").fetchall()
        print(bills)
        return admin_menu(name)
    elif move == '3':
        put_bill_admin()
    elif move == '4':
        take_bill_admin()
    elif move == '0':
        return input_menu()
    else:
        print('Введено некоректне значення')
        return admin_menu(name)


def start(name):
    print('1. Баланс\n'
          '2. Поповнити баланс\n'
          '3. Зняти кошти\n'
          '0. Вихід')
    move = input('Введіть цифру: ')
    if move == '1':
        print(balance(name))
        return start(name)
    elif move == '2':
        amount = input('Введіть суму: ')
        put_money(name, amount)
    elif move == '3':
        amount = input('Введіть суму: ')
        take_money(name, amount)
    elif move == '0':
        return input_menu()
    else:
        print('Введено некоректне значення')
        return start(name)


if __name__ == "__main__":
    input_menu()
    conn.close()
