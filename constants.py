PRODUCT_CATEGORY_URL = 'https://www.ozon.ru/category/smartfony-15502/'
SORTING_PRODUCTS_IN_CATEGORY_BY = 'rating'
PRODUCT_CATEGORY_PAGES_LIMIT_TO_PARSE = 4
PRODUCT_PAGE_URL_MARKER = 'asb2'
XPATH_TO_PRODUCT_DATA = (
    '/html/body/div[1]/div/div[1]/div[6]/div/div[1]/div[3]/div[2]/div/div/div[3]/div/div[2]'
)
PRODUCT_PARAMS_TO_KEY_TO_LOOK_FOR = {
    'Операционная система': 'os',
    'Версия iOS': 'version',
    'Версия Android': 'version',
}
ITEMS_AMOUNT_FOR_DISTRIBUTION = 100
