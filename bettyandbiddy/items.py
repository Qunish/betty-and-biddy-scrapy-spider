# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BettyandbiddyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_original_price = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_imagelink = scrapy.Field()
    product_link = scrapy.Field()
    pass


class BettyandbiddyItem_pv(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_description = scrapy.Field()
    image_link = scrapy.Field()
    product_size = scrapy.Field()
    product_material = scrapy.Field()
    pass
