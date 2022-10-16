"""Створіть ф-цiю, яка буде отримувати довільні рядки
на зразок цього та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно)
-> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел
та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)"""


def check_string(string):
    l_str = len(string)

    if 30 <= l_str <= 50:
        cnt_d = 0
        cnt_alp = 0
        for i in string:
            if i.isdigit():
                cnt_d += 1
            elif i.isalpha():
                cnt_alp += 1
        print(f'Довжина: {l_str}, цифр: {cnt_d}, букв: {cnt_alp}')
    elif l_str < 30:
        sum_digit = 0
        str_digit = ''
        for i in string:
            if i.isdigit():
                sum_digit += int(i)
                str_digit += i
        print(f'{str_digit} -> сума цифр: {sum_digit}')
    else:
        sign = ''
        for i in string:
            if not i.isalnum() and not i.isspace():
                sign += i
        print(sign, '-> кількість знаків', len(sign))


check_string(input('Enter string: '))
