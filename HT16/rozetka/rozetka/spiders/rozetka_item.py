#!/usr/bin/env python3
import scrapy


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua']
    BASE_URL = 'http://rozetka.com.ua/'
    API_URL = f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?goodsId='
    # start_urls = ['https://rozetka.com.ua/ua/mobile-phones/c80003/page=2/']
    # category = None

    def start_requests(self):
        category = getattr(self, 'category', None)
        if category is not None:
            self.BASE_URL = f'{self.BASE_URL}{category}'
            yield scrapy.Request(
                url=self.BASE_URL,
                callback=self.parse_pages
            )

    def parse_pages(self, response):
        for item in list(self.parse_id(response)):
            print(item)
            yield item
        last_page = response.css('[class="pagination__link ng-star-inserted"]::text')[-1].get()
        for page in range(2, 1 + int(last_page)):
            yield scrapy.Request(
                url=f'{self.BASE_URL}page={page}/',
                callback=self.parse_id
            )

    def parse_id(self, response):
        for product_id in response.css('.ng-star-inserted .goods-tile__inner::attr(data-goods-id)').getall():
            yield scrapy.Request(
                url=f'{self.API_URL}{product_id}',
                callback=self.parse
            )

    def parse(self, response, **kwargs):
        item_info = response.json()['data']
        yield {
            'name': item_info['name'],
            'price': item_info['price'],
            'category': item_info['title'],
            'brand': item_info['brand'],
            'title': item_info['title'],
            'href': item_info['href']
        }


