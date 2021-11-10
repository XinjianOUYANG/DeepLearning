import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from porscheHD.items import PorschehdItem

class Porsche911hdSpider(CrawlSpider):
    name = 'porsche911HD'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/162.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/162.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        category = response.xpath('//div[@class="uibox"]/div[@class="uibox-title"]/text()').get()
        srcs = response.xpath('//div[@class="uibox"]//ul/li/a/img/@src').getall()
        srcs = list(map(lambda x: x.replace('240x180_0_q95_c42_', ''), srcs))
        image_urls = list(map(lambda x: response.urljoin(x), srcs))
        item = PorschehdItem(category=category, image_urls=image_urls)
        yield item

