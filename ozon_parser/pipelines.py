from scrapy.exporters import JsonLinesItemExporter

from constants import PRODUCT_PARAMS_TO_KEY_TO_LOOK_FOR


class ProductDataPipeline:
    """
    Поиск и обработка данных каждого товара.
    Сохранение данных товара (операционная система, версия ос)
    в отдельный файл os_and_version.json.
    """

    def __init__(self):
        self.file = open('os_and_version.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        os_and_version = {}
        for i, parameter in enumerate(item.get('product_tech')):
            key = PRODUCT_PARAMS_TO_KEY_TO_LOOK_FOR.get(parameter)
            if key:
                os_and_version[key] = item.get('product_tech')[i+1]
        del item['product_tech']
        if ('os' in os_and_version and
            'version' in os_and_version and
                any(os_and_version)):
            item['os_and_version'] = os_and_version
        if item.get('os_and_version'):
            self.exporter.export_item(item.get('os_and_version'))
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
