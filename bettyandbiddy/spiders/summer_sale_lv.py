import scrapy
from ..items import BettyandbiddyItem
import pymongo

class BettyandbiddySpider(scrapy.Spider):
    name = "summer_sale_lv"
    page_number = 2
    start_urls = [
        "https://bettyandbiddy.com/collections/summer-sale?page=1"
    ]

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn["bettyandbiddy_db"]
        self.collection = db["summer_sale"]

    def parse(self, response):
        items = BettyandbiddyItem()
        all_products = response.css(".on-sale")

        for product in all_products:
            product_name = product.css(".boost-pfs-filter-product-item-title::text").extract_first()
            product_original_price = product.css("s .money::text").extract_first()
            product_sale_price = product.css(".boost-pfs-filter-product-item-sale-price .money::text").extract_first()
            # product_imagelink = product.css(".lazyloaded::attr(data-srcset)").get()
            base_product_url = product.css(".boost-pfs-filter-product-item-title::attr(href)").extract_first().replace("#","")
            product_link = ("https://bettyandbiddy.com")+base_product_url

            items["product_name"] = product_name
            items["product_original_price"] = product_original_price
            items["product_sale_price"] = product_sale_price
            # items["product_imagelink"] = product_imagelink
            items["product_link"] = product_link

            self.collection.insert_one(dict(items))
            yield items


        next_page = "https://bettyandbiddy.com/collections/summer-sale?page=" + str(BettyandbiddySpider.page_number)
        if BettyandbiddySpider.page_number < 6:
            BettyandbiddySpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)