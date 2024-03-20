import json

import scrapy
from scrapy_selenium import SeleniumRequest

from ozon_parser.items import ProductDataItem
from constants import XPATH_TO_PRODUCT_DATA


class ProductDataSpider(scrapy.Spider):
    """Парсер параметров товара."""

    name = "product_data_spider"
    custom_settings = {
        'ITEM_PIPELINES': {
            'ozon_parser.pipelines.ProductDataPipeline': 100,
        }
    }

    def start_requests(self):
        with open('product_links.json', 'r') as file:
            data = json.load(file)
        urls = [item['url'] for item in data]
        for url in urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=1)

    def parse(self, response):
        item = ProductDataItem()
        item['product_tech'] = response.xpath(
            f"{XPATH_TO_PRODUCT_DATA}//text()"
        ).getall()
        yield item
