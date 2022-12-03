from rozetka_api import RozetkaAPI
from data_operations import CsvOperation, DataBaseOperation


if __name__ == '__main__':
    rozetka = RozetkaAPI()
    db = DataBaseOperation()
    items = CsvOperation().take_item_id('items_id.csv')
    for item_id in items:
        data = rozetka.get_item_data(item_id)
        db.save_in_db(data)


