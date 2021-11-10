import scrapy
import json

class IpproxytestSpider(scrapy.Spider):
    name = 'IPProxyTest'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        origin = json.loads(response.text)['origin']
        print('=' * 40)
        print(origin)
        print('=' * 40)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)
