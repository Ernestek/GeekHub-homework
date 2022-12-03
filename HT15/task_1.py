"""
1. Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт
"https://www.expireddomains.net/domain-lists/"
вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів
з усіма відповідними колонками - доменів там буде десятки тисяч (звичайно
ураховуючи пагінацію). Всі отримані значення зберегти в CSV файл.
"""
import csv
from dataclasses import dataclass, fields, astuple

from random import randrange
from time import sleep
import requests
from bs4 import BeautifulSoup


@dataclass
class Domain:
    domain:  str
    BL:      str
    DP:      int
    ABY:     str
    ACR:     int
    Dmoz:    str
    C:       str
    N:       str
    O:       str
    D:       str
    Reg:     int
    RTD:     str
    Traffic: int
    Price:   str
    Bids:    int
    Endtime: str


class DomainsParser:
    BASE_URL = 'https://www.expireddomains.net/sedo-expired-domains/'
    DOMAIN_FIELDS = [field.name for field in fields(Domain)]
    DOMAINS_OUTPUT_CSV_PATH = 'domains.csv'

    session = requests.Session()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    headers = {'user-agent': user_agent}

    def parser_single_domain(self, domain_soup: BeautifulSoup) -> Domain:
        return Domain(
            domain=domain_soup.select_one('.field_domain a')['title'],
            BL=domain_soup.select_one('.field_bl a')['title'],
            DP=int(domain_soup.select_one('.field_domainpop a')['title']),
            ABY=domain_soup.select_one('.field_abirth').text,
            ACR=int(domain_soup.select_one('.field_aentries a').text),
            Dmoz=domain_soup.select_one('.field_dmoz').text,
            C=domain_soup.select_one('.field_statuscom span').text,
            N=domain_soup.select_one('.field_statusnet span').text,
            O=domain_soup.select_one('.field_statusorg span').text,
            D=domain_soup.select_one('.field_statusde span').text,
            Reg=int(domain_soup.select_one('.field_statustld_registered').text),
            RTD=domain_soup.select_one('.field_related_cnobi').text,
            Traffic=int(domain_soup.select_one('.field_traffic a')['title']),
            Price=domain_soup.select_one('.field_price a').text,
            Bids=int(domain_soup.select_one('.field_bids a').text),
            Endtime=domain_soup.select_one('.field_endtime a').text
        )

    def get_page_domains(self, page_soup: BeautifulSoup) -> [Domain]:
        domains = page_soup.select('tbody tr')
        print(len(domains))
        return [self.parser_single_domain(domain_soup) for domain_soup in domains]

    def get_all_domains(self) -> [Domain]:
        page = self.session.get(self.BASE_URL, headers=self.headers, stream=True).content
        first_page_soup = BeautifulSoup(page, 'lxml')
        print('1')
        sleep(randrange(6, 10))
        all_domains = self.get_page_domains(first_page_soup)

        for start in range(25, 301, 25):
            page = self.session.get(self.BASE_URL, params={'start': int(start)},
                                    headers=self.headers, stream=True).content
            sleep(randrange(5, 8))
            soup = BeautifulSoup(page, 'lxml')
            print(start)
            all_domains.extend(self.get_page_domains(soup))

        return all_domains

    def write_product_to_csv(self, products: [Domain]):
        with open(self.DOMAINS_OUTPUT_CSV_PATH, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.DOMAIN_FIELDS)
            writer.writerows([astuple(product) for product in products])
        return


if __name__ == '__main__':
    parser = DomainsParser()
    domains = parser.get_all_domains()
    parser.write_product_to_csv(domains)
