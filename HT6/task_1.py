"""1. Створіть функцію, всередині якої будуть
записано СПИСОК із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два - обов'язкових
(<username> та <password>) і третій - необов'язковий
параметр <silent> (значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException
        (його також треба створити =))"""


class LoginException(Exception):
    pass


def user_verification(username, password, silent=False):
    users = [('user1', 'pass1'), ('user2', 'pass2'), ('user3', 'pass3'),
             ('user4', 'pass4'), ('user5', 'pass5')]
    check = (username, password)
    if check in users:
        return True
    else:
        if silent:
            return False
        else:
            raise LoginException('Login Exception')


print(user_verification('user1', 'pass'))
