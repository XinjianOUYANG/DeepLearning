import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsbk_crawl.items import QsbkCrawlItem


class QsbkCrawlSpiderSpider(CrawlSpider):
    name = 'qsbk_crawl_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/text/page/\d+/'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/article/\d+'), callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):
        author = response.xpath('//div[@class="side-user-top"]/span[@class="side-user-name"]/text()').get()
        content = response.xpath('//div[@id="single-next-link"]/div[@class="content"]//text()').getall()
        content = "".join(content).strip()
        print(content)
        item = QsbkCrawlItem(author=author, content=content)
        yield item




