import csv
import urllib.request


def data_order() -> list:
    url = 'https://robotsparebinindustries.com/orders.csv'
    response = urllib.request.urlopen(url)
    lines = [line.decode('utf-8') for line in response.readlines()]
    order = list(csv.reader(lines))[1:]
    return order
