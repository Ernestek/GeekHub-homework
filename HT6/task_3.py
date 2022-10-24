"""3. На основі попередньої функції (скопіюйте кусок коду)
створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних
   видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і,
   користуючись валідатором, перевірить ці дані і надрукує для кожної
   пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)"""


class NameException(Exception):
    pass


class PasswordException(Exception):
    pass


def validation(username, password):
    if len(username) < 3 or len(username) > 51:
        raise NameException('name length should be >2 and <51')
    if len(password) < 8:
        raise PasswordException('the password is too short')
    elif not any(map(str.isdigit, password)):
        raise PasswordException('password must have at least one digit')
    elif any(map(str.isspace, password)):
        raise PasswordException('password must not have spaces')
    return True


users = [('us', 'password1'), ('user2', 'password 2'), ('user3', 'pass3'),
         ('user4', 'password4')]

for user in users:

    try:
        validation(user[0], user[1])
    except NameException as err:
        status = err
        print(f'Name: {user[0]}\nPassword: {user[1]}\nStatus: {status}')
    except PasswordException as err:
        status = err
        print(f'Name: {user[0]}\nPassword: {user[1]}\nStatus: {status}')
    else:
        print(f'Name: {user[0]}\nPassword: {user[1]}\nStatus: OK')
    finally:
        print('----------')
