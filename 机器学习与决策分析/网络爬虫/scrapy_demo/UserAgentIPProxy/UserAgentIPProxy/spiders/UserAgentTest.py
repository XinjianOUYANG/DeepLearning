import scrapy
import json


class UseragenttestSpider(scrapy.Spider):
    name = 'UserAgentTest'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent']
        print('=' * 40)
        print(user_agent)
        print('=' * 40)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)

