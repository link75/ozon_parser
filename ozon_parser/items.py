import scrapy


class ProductDataItem(scrapy.Item):
    product_tech = scrapy.Field()
    os_and_version = scrapy.Field()
