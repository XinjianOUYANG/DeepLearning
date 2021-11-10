import scrapy

class PorscheItem(scrapy.Item):
    category = scrapy.Field()
    image_urls = scrapy.Field()

