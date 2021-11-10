import scrapy


class MyscrapytestSpider(scrapy.Spider):
    name = 'myscrapyTest'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
