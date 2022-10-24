"""4. Створіть функцію <morse_code>, яка приймає на вхід
рядок у вигляді коду Морзе та виводить декодоване значення
(латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive (на ваш розсуд -
    великими чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї,
    дужки, лапки тощо використовуватися не будуть. Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..-- -...   .. ...   .... . .-. .
    результат: GEEKHUB IS HERE"""


def morse_code(string):
    MORSE_CODE_DICT = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                       '-..': 'D', '.': 'E', '..-.': 'F',
                       '--.': 'G', '....': 'H', '..': 'I',
                       '.---': 'J', '-.-': 'K', '.-..': 'L',
                       '--': 'M', '-.': 'N', '---': 'O',
                       '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                       '...': 'S', '-': 'T', '..--': 'U',
                       '...-': 'V', '.--': 'W', '-..-': 'X',
                       '-.--': 'Y', '--..': 'Z', '': ' ',
                       '...---...': 'SOS'}

    string = string.split(' ')
    message = []
    for code in string:
        message.append(MORSE_CODE_DICT[code])

    result = ' '.join(''.join(message).split('  '))
    return result


print(morse_code('--. . . -.- .... ..-- -...   .. ...   .... . .-. .'))
print(morse_code('...---...'))
