"""
- data_operations.py з класами CsvOperations та DataBaseOperations.
CsvOperations містить метод для читання даних. Метод для читання
приймає аргументом шлях до csv файлу де в колонкі ID записані як
валідні, так і не валідні id товарів з сайту. DataBaseOperations
містить метод для запису даних в sqlite3 базу і відповідно приймає
дані для запису. Всі інші методи, що потрібні для роботи мають бути
приватні/захищені.
"""
import csv
import sqlite3


# help(csv)
class CsvOperation:

    @staticmethod
    def take_item_id(way_file: str):
        with open(way_file, 'r') as file:
            items = csv.DictReader(file)
            for i in items:
                yield i['id']


class DataBaseOperation:

    def __init__(self):
        self.__conn = sqlite3.connect('rozetka_items_data.db')
        self.__cursor = self.__conn.cursor()

    def __connect_db(self):
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS ITEMS 
                (ID             PRIMARY KEY        NOT NULL,   
                TITLE           TEXT               NOT NULL,
                OLD_PRICE       INT                NOT NULL,
                CURRENT_PRICE   INT DEFAULT 0,
                HREF            TEXT               NOT NULL,
                BRAND           TEXT               NOT NULL,
                CATEGORY        TEXT               NOT NULL);''')
        self.__conn.commit()

    def save_in_db(self, item_data: dict):
        print(item_data)
        if item_data:
            self.__connect_db()

            self.__cursor.execute("INSERT OR IGNORE INTO ITEMS (id,title,old_price,current_price,href,brand,category) "
                                  "VALUES ((?), (?), (?), (?), (?), (?), (?))",
                                  (item_data['item_id'], item_data['title'], item_data['old_price'],
                                   item_data['current_price'], item_data['href'], item_data['brand'],
                                   item_data['category']))
            self.__conn.commit()


if __name__ == '__main__':
    item_id = CsvOperation
    for i in item_id.take_item_id('items_id.csv'):
        print(i)
