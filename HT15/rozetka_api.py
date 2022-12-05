"""
- rozetka_api.py, де створти клас RozetkaAPI, який буде
містити 1 метод get_item_data, який на вхід отримує id
товара з сайту розетки та повертає словник з такими даними:
item_id (він же і приймається на вхід), title, old_price,
current_price, href (лінка на цей товар на сайті), brand,
category. Всі інші методи, що потрібні для роботи мають
бути приватні/захищені.
"""
import requests


class RozetkaAPI:
    session = requests.Session()

    def get_item_data(self, item_id: str) -> dict:
        url = f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?goodsId={item_id}'
        response = self.session.get(url=url)
        success = response.json()['success']
        if not success:
            print('Не знайдено товару з id: ', item_id)
        if success:
            return dict(
                item_id=response.json()['data']['id'],
                title=response.json()['data']['title'],
                old_price=response.json()['data']['old_price'],
                current_price=response.json()['data']['price'],
                href=response.json()['data']['href'],
                brand=response.json()['data']['brand'],
                category=response.json()['data']['breadcrumbs'][0]['title']
            )


