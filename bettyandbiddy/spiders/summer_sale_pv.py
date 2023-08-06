import scrapy
from ..items import BettyandbiddyItem_pv
import pymongo


class BettyandbiddySpider_pv(scrapy.Spider):
    name = "summer_sale_pv"

    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn["bettyandbiddy_db"]
        self.collection = db["summer_sale"]
        self.start_urls = [document['product_link'] for document in self.collection.find()]

    def parse(self, response):
        item = BettyandbiddyItem_pv()
        product_description = response.css("#template-product p:nth-child(1)::text").get()
        product_material = response.css("p:nth-child(2)::text").get()
        product_size = response.css("p~ p+ p::text").get()       
        base_image_link = response.css("img::attr(src)").get()
        image_link = "https:" + base_image_link
        
        item['product_description'] = product_description
        item["image_link"] = image_link
        item["product_material"] = product_material
        item["product_size"] = product_size

        self.collection.update_one(
            {'product_url': response.url},
            {'$set': dict(item)},
            upsert=True
        )
        yield item
