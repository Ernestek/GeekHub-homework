"""
2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал
- початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати
(або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
"""
import json
from datetime import datetime, timedelta
import requests


def get_currency_rate_in_range():
    date = input('Enter date (dd.mm.yyyy) or range date (dd.mm.yyyy-dd.mm.yyyy)\n').split('-')
    date_start = date[0]
    date_end = date[1] if len(date) > 1 else 0
    try:
        date_start = datetime.strptime(date_start, '%d.%m.%Y')
    except ValueError:
        print('Не коректно введені дати')
        return

    if date_end:
        try:
            date_end = datetime.strptime(date_end, '%d.%m.%Y')
            if (date_end - date_start).days < 0:
                print('Не коректно введені дати')
                return
        except ValueError:
            print('Не коректно введені дати')
            return
        date_range = [(date_start + timedelta(days=x)).strftime('%d.%m.%Y') for x in
                      range(0, (date_end - date_start).days + 1)]
        for day in date_range:
            get_currency_rate(day)
    else:
        get_currency_rate(datetime.strftime(date_start, '%d.%m.%Y'))


def get_currency_rate(date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Не знайдено інформацію за {date}')
        return
    print(date)
    response_content = response.content
    currency_info = json.loads(response_content)
    for currency in currency_info['exchangeRate']:
        if currency['currency'] in ('USD', 'EUR', 'GBP', 'PLN'):
            print(f'{currency["currency"]} продаж: {currency["saleRate"]} купівля: {currency["purchaseRate"]}')


if __name__ == '__main__':
    get_currency_rate_in_range()
