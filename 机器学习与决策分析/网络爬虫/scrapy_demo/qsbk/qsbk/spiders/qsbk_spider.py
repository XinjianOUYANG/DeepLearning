import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    Base_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        duanzi_divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for duanzi_div in duanzi_divs:
            author = duanzi_div.xpath('.//div[@class="author clearfix"]//h2/text()').get().strip()
            content = duanzi_div.xpath('.//div[@class = "content"]/span/text()').getall()
            content = ''.join(content).strip()
            item = QsbkItem(author=author, content=content)
            yield item

        next_url = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href').get()
        if not next_url:
            return
        else:
            next_url = self.Base_domain + next_url
            yield scrapy.Request(next_url, callback=self.parse)





import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    Base_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        # duanzi_divs是SelectorList类型
        duanzi_divs = response.xpath('//div[@class="col1 old-style-col1"]/div')
        for duanzi_div in duanzi_divs:
            # duanzi_div是Selector类型
            author = duanzi_div.xpath('.//div[@class="author clearfix"]//h2/text()').get().strip()
            content = duanzi_div.xpath('.//div[@class = "content"]/span/text()').getall()
            content = ''.join(content).strip()
            # 运用items来保存参数的好处是：不会多传或者少传数据，另外用类显得更专业，
            # 但这里返回的item是qsbk.items.QsbkItem数据类型，其不是一个字典数据类型的
            item = QsbkItem(author=author, content=content)
            yield item

        next_url = response.xpath('//ul[@class="pagination"]//li[last()]/a/@href').get()
        if not next_url:
            return
        else:
            next_url = self.Base_domain + next_url
            yield scrapy.Request(next_url, callback=self.parse)



