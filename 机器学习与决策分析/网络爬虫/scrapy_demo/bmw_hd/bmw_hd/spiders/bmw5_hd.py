import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bmw_hd.items import BmwHdItem


class Bmw5HdSpider(CrawlSpider):
    name = 'bmw5_hd'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        category = response.xpath('//div[@class="uibox"]/div[@class="uibox-title"]/text()').get()
        srcs = response.xpath('//div[@class="uibox"]//ul/li/a/img/@src').getall()
        srcs = list(map(lambda x: x.replace('240x180_0_q95_c42_', ''), srcs))
        image_urls = list(map(lambda x: response.urljoin(x), srcs))
        yield BmwHdItem(category=category, image_urls=image_urls)








