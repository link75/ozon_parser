import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy_selenium import SeleniumRequest

from constants import (PRODUCT_CATEGORY_PAGES_LIMIT_TO_PARSE,
                       PRODUCT_CATEGORY_URL, PRODUCT_PAGE_URL_MARKER,
                       SORTING_PRODUCTS_IN_CATEGORY_BY)


class ProductLinksSpider(scrapy.Spider):
    """
    Парсер ссылок на товары.
    Сохранение списка ссылок в отдельный файл
    product_links.json.
    """

    name = "product_links_spider"
    urls = [f'{PRODUCT_CATEGORY_URL}?page={x}&'
            f'sorting={SORTING_PRODUCTS_IN_CATEGORY_BY}'
            for x in range(1, PRODUCT_CATEGORY_PAGES_LIMIT_TO_PARSE + 1)]
    custom_settings = {
        'FEEDS': {
            'product_links.json': {'format': 'json', 'overwrite': True}
        },
        'ITEM_PIPELINES': {},
    }

    def start_requests(self):
        for url in self.urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=1)

    def parse(self, response):
        link_extractor = LinkExtractor()
        for link in link_extractor.extract_links(response):
            if PRODUCT_PAGE_URL_MARKER in link.url:
                yield {'url': link.url}
