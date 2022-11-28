"""
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної
інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
"""
import csv
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


@dataclass
class Quotes:
    author: str
    quote: str
    tags: list
    born_date: str
    born_location: str
    author_description: str


class QuotesParser:
    BASE_URL = 'http://quotes.toscrape.com/'
    QUOTES_OUTPUT_CSV_PATH = 'quotes.csv'
    QUOTES_FIELDS = [field.name for field in fields(Quotes)]

    def get_10_page_quotes(self) -> [Quotes]:
        all_quotes = []
        for number in range(1, 11):
            print(number)
            number_page = f'page/{number}/'
            page_url = urljoin(self.BASE_URL, number_page)
            page = requests.get(page_url).content
            all_quotes.extend(self.get_quotes(page))
        return all_quotes

    def get_quotes(self, page) -> [Quotes]:
        soup = BeautifulSoup(page, 'lxml')
        quotes = soup.select('.quote')
        return [self.parser_single_quote(quote_soup) for quote_soup in quotes]

    def info_about_author(self, about_url) -> dict:
        page = requests.get(urljoin(self.BASE_URL, about_url)).content
        info_soup = BeautifulSoup(page, 'lxml')
        return dict(
            born_date=info_soup.select_one('.author-born-date').text,
            born_location=info_soup.select_one('.author-born-location').text,
            author_description=info_soup.select_one('.author-description').text
        )

    def parser_single_quote(self, quote_soup: BeautifulSoup) -> Quotes:
        tags = list(map(lambda tag: tag.text, quote_soup.select('.tags > a.tag')))

        about_url = quote_soup.select_one('span [href]').attrs.get('href')
        about = self.info_about_author(about_url)

        return Quotes(
            author=quote_soup.select_one('small.author').text,
            quote=quote_soup.select_one('.text').text,
            tags=tags,
            born_date=about['born_date'],
            born_location=about['born_location'],
            author_description=about['author_description']
        )

    def write_quotes_to_csv(self, quotes: [Quotes]):
        with open(self.QUOTES_OUTPUT_CSV_PATH, 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(self.QUOTES_FIELDS)
            writer.writerows([astuple(quote) for quote in quotes])
        return


if __name__ == '__main__':
    parser = QuotesParser()
    quotes = parser.get_10_page_quotes()
    parser.write_quotes_to_csv(quotes)
