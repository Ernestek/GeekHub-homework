import csv
import urllib.request

url = 'https://robotsparebinindustries.com/orders.csv'
response = urllib.request.urlopen(url)
lines = [line.decode('utf-8') for line in response.readlines()]
data_order = csv.reader(lines)
next(data_order)

