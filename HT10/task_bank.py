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


def take_bill(arr):
    for i in arr:
        amount = i[1]
        name = str(i[0])
        cursor.execute("UPDATE ATM SET AMOUNT = AMOUNT - (?) WHERE NAME = (?)",
                       (amount, name))
        conn.commit()


def calculate_sum_bill(amount, bill_list):
    bill_list.sort(reverse=True)

    if len(bill_list) < 1:
        return
    start_sum = amount
    result = []

    for k, v in bill_list:
        k = int(k)

        if v == 0:
            continue
        if amount < k:
            continue
        if amount // k <= v:

            result.append((k, amount // k))
            amount -= amount // k * k
            continue
        else:

            result.append((k, v))
            amount -= v * k
            continue

    if amount > 0:
        result = [(result[0][0], result[0][1] - 1)]
        start_sum -= result[0][1] * result[0][0]
        try:
            result.extend(calculate_sum_bill(start_sum, bill_list[1:]))
        except TypeError:
            return

    for i in result:
        if i[1] == 0:
            result.remove(i)

    return result


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


def check_user(name):
    list_users = cursor.execute("SELECT NAME FROM USERS").fetchall()
    for user in list_users:
        if name == user[0]:
            return True


def registration():
    while True:
        name = input('0. Exit\n'
                     'Come up with a name: ')
        if name == '0':
            break

        cursor.execute("SELECT id FROM USERS ORDER BY id DESC ")
        id_sel = cursor.fetchone()[0] + 1

        if check_user(name):
            print('This name is already used')
            continue
        if not validation_name(name):
            continue
        for _ in range(6):
            password = input('Come up with a password: ')
            if not validation_password(password):
                continue
            cursor.execute("INSERT INTO USERS (id,NAME,PASSWORD) VALUES ((?), (?), (?))",
                           (id_sel, name, password))
            conn.commit()
            print(f'Вітання, {name}, ')
            user_menu(name)
            return
        print('Невдала спроба')
        break
    return


def authorization():
    while True:
        name = input('Введіть логін: ')
        password = input('Введіть пароль: ')
        state = False

        if name == 'admin' and password == 'admin':
            """***********"""
            admin_menu(name)
            return

        list_name = cursor.execute("SELECT NAME, PASSWORD FROM USERS").fetchall()

        for user in list_name:
            if name == user[0] and password == user[1]:
                state = True
        if state:
            user_menu(name)
            return
        else:
            print("Ім'я або пароль введено неправильно")
            break
    return


def user_balance(name):
    money = cursor.execute("SELECT BALANCE FROM USERS WHERE NAME=(?)", (name,)).fetchone()
    return money[0]


def transaction(name, amount, operation, *args):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
    if name == 'admin':
        operation = 'внесено' if operation == '+' else 'вилучено'
        now = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
        record = f'{now} {operation} {amount} купюр, номиналом {args[0]}\n'
        cursor.execute("UPDATE USERS SET TRANSACTIONS = TRANSACTIONS || (?) WHERE NAME = (?)",
                       (record, 'admin'))
        conn.commit()
    else:
        record = f'{now}: {operation}{amount}\n'
        cursor.execute("UPDATE USERS SET TRANSACTIONS = TRANSACTIONS || (?) WHERE NAME = (?)",
                       (str(record), name))
        conn.commit()


def check_transactions(name):
    data = cursor.execute("SELECT TRANSACTIONS FROM USERS WHERE name = (?)", (name,))
    print(data.fetchone()[0])
    input('Натисни ENTER щоб повернутись назад')


def take_money(name, amount):
    while True:
        try:
            amount = float(amount)
        except ValueError:
            print('Введено некоректне значення')
            break

        if amount < 0:
            print('Некоректне значення')
            break

        my_balance = user_balance(name)
        if my_balance < amount:
            print('Недостатньо коштів')
            print(f'Баланс: {my_balance}')
            break

        if atm_balance() < amount:
            print('Недостатньо коштів в банкоматі\n'
                  f'Максимальна сума зняття: {atm_balance()}')
            break
        change = amount % 10
        amount -= change
        bill_list = cursor.execute("SELECT name, amount FROM ATM").fetchall()
        check = calculate_sum_bill(int(amount), bill_list)
        if check is None:
            print('Неполиво зняти таку сумму')
            break
        print(check)
        take_bill(check)

        print(f'Знято {int(amount)}')
        cursor.execute("UPDATE USERS SET balance = balance - (?) WHERE NAME = (?)",
                       (amount, name))
        print(f'Баланс: {user_balance(name)}')

        transaction(name, amount, operation='-')
        break
    return


def put_money(name, amount):
    while True:
        try:
            amount = int(amount)
        except ValueError:
            print('Введено некоректне значення')
            break

        if amount < 0:
            print('Некоректне значення')
            break

        change = amount % 10
        amount -= change
        cursor.execute("UPDATE USERS SET balance = balance + (?) WHERE NAME = (?)",
                       (int(amount), name))
        print(f'Внесено: {amount}\n'
              f'Баланс: {user_balance(name)}\n')
        if change > 0:
            print(f'Решта: {change}')

        transaction(name, amount, operation='+')
        break
    return


def atm_balance():
    bills = cursor.execute("SELECT name, amount FROM ATM").fetchall()
    result = 0
    for i in bills:
        result += int(i[0]) * i[1]
    return result


def take_bill_admin():
    while True:
        num = ('10', '20', '50', '100', '200', '500', '1000')
        bill = input('0. Назад\n'
                     'Введіть номінал: ')
        if bill == '0':
            break
        if bill not in num:
            print('Невідома купюра')
            continue
        try:
            amount = int(input('Введіть кількість: '))
        except ValueError:
            print('Некоректні дані')
            continue
        else:
            if amount < 0:
                print('Некоректні дані')
                continue
            bank_amount_bill = cursor.execute("SELECT amount FROM ATM WHERE name = (?)",
                                              (bill,)).fetchone()
            if amount > bank_amount_bill[0]:
                print(f'Недостатньо купюр, наявна кількість: {bank_amount_bill[0]}')
                continue
            cursor.execute("UPDATE ATM SET amount = amount - (?) WHERE name = (?)",
                           (amount, bill))
            transaction('admin', amount, '-', bill)
        break
    return


def put_bill_admin():
    while True:
        num = ('10', '20', '50', '100', '200', '500', '1000')
        bill = input('0. Назад\n'
                     'Введіть номінал: ')
        if bill == '0':
            return
        if bill not in num:
            print('Невідома купюра')
            continue
        try:
            amount = int(input('Введіть кількість: '))
        except ValueError:
            print('Некоректні дані')
            continue
        else:
            if amount < 0:
                print('Некоректні дані')
                continue

            cursor.execute("UPDATE ATM SET amount = amount + (?) WHERE name = (?)",
                           (amount, bill))
            transaction('admin', amount, '+', bill)
        break
    return


def input_menu():
    while True:
        move = input('1. Авторизація\n'
                     '2. Реєстрація\n'
                     '0. Вихід\n'
                     'Введіть цифру: ')
        if move == '1':
            authorization()
            continue
        elif move == '2':
            registration()
            continue
        elif move == '0':
            exit(0)
            return
        else:
            print('Введено некоректне значення')
            continue


def admin_menu(name):
    while True:
        print('1. Баланс банкомату\n'
              '2. Кількість купюр\n'
              '3. Внести купюри\n'
              '4. Вилучити купюри\n'
              '5. История операцій\n'
              '6. История операцій користувача\n'
              '0. Вихід')
        move = input('Введіть цифру: ')
        if move == '1':
            print(atm_balance())
            continue
        elif move == '2':
            bills = cursor.execute("SELECT name, amount FROM ATM").fetchall()
            print(bills)
            continue
        elif move == '3':
            put_bill_admin()
            continue
        elif move == '4':
            take_bill_admin()
            continue
        elif move == '5':
            check_transactions(name)
            continue
        elif move == '6':
            name = input('Введіть логін корустувача')
            if check_user(name):
                check_transactions(name)
            else:
                print('Користувача не існує')
            continue
        elif move == '0':
            return
        else:
            print('Введено некоректне значення')
            continue


def user_menu(name):
    while True:
        print('1. Баланс\n'
              '2. Поповнити баланс\n'
              '3. Зняти кошти\n'
              '4. История операцій\n'
              '0. Вихід')
        move = input('Введіть цифру: ')
        if move == '1':
            print(user_balance(name))
            continue
        elif move == '2':
            amount = input('Введіть суму: ')
            put_money(name, amount)
            continue
        elif move == '3':
            amount = input('Введіть суму: ')
            take_money(name, amount)
            continue
        elif move == '4':
            check_transactions(name)
            continue
        elif move == '0':
            return
        else:
            print('Введено некоректне значення')
            continue


if __name__ == "__main__":
    input_menu()
    conn.close()
