BOT_NAME = "ozon_parser"

SPIDER_MODULES = ["ozon_parser.spiders"]
NEWSPIDER_MODULE = "ozon_parser.spiders"

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = None
SELENIUM_DRIVER_ARGUMENTS = ['--headless']

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
