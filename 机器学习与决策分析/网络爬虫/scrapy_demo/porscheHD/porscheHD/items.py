import scrapy

class PorschehdItem(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

