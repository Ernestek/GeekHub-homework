"""2. Створіть функцію для валідації пари ім'я/пароль
    за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам -
   породити виключення із відповідним текстом."""


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


validation('user', 'password1')
