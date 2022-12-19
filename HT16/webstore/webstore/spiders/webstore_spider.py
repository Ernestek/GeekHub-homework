import scrapy
from bs4 import BeautifulSoup


class WebstoreSpider(scrapy.Spider):
    name = 'webstore_spider'
    allowed_domains = ['chrome.google.com']
    BASE_URL = 'https://chrome.google.com/webstore/sitemap'

    def start_requests(self):
        yield scrapy.Request(
            url=self.BASE_URL,
            callback=self.parse_map
        )

    def parse_map(self, response):
        soup = BeautifulSoup(response.body, 'xml')
        for url in soup.select('sitemap loc'):
            yield scrapy.Request(
                url=url.text,
                callback=self.parse_urls
            )

    def parse_urls(self, response):
        soup = BeautifulSoup(response.body, 'xml')
        for url in soup.select('url loc'):
            yield scrapy.Request(
                url=url.text,
                callback=self.parse
            )

    def parse(self, response, **kwargs):
        yield {
            'id': response.css('[property="og:url"]::attr(content)').get()[-32:],
            'name': response.css('.e-f-w::text').get(),
            'description': response.css('[name="Description"]::attr(content)').get()
        }
