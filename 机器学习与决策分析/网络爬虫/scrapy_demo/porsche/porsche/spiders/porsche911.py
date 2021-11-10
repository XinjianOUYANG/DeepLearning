import scrapy
from porsche.items import PorscheItem

class Porsche911Spider(scrapy.Spider):
    name = 'porsche911'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/162.html']

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            category = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
            print('=' * 40)
            print(category)

            urls = uibox.xpath('.//ul/li/a/img/@src').getall()
            urls = list(map(lambda x: 'https:' + x, urls))
            print(urls)
            print('=' * 40)

            item = PorscheItem(category=category, image_urls=urls)
            yield item



# class Porsche911Spider(scrapy.Spider):
#     name = 'porsche911'
#     allowed_domains = ['car.autohome.com.cn']
#     start_urls = ['https://car.autohome.com.cn/price/brand-40.html/']
#
#     def parse(self, response):
#         uiboxs = response.xpath('//div[@class="uibox"]')[1:]
#         for uibox in uiboxs:
#             category = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
#             # 由于最后“改装”栏所在的div中的class属性为"uibox-con carpic-list03  border-b-solid"，而之前的div中的class
#             # 属性为"uibox-con carpic-list03"，因此需要用以下命令获得所有栏目中的图片url
#             # urls = uibox.xpath('.//div[contains(@class,"uibox-con carpic-list03")]/ul/li/a/img/@src').getall()
#             # 或者将div去掉，用以下命令更简单
#             urls = uibox.xpath('.//ul/li/a/img/@src').getall()
#             urls = list(map(lambda x: 'https:' + x, urls))
#
#             # 或者用以下命令来拼接
#             # urls = list(map(lambda x: response.urljoin(x), img_urls))
#
#             item = BmwItem(category=category, image_urls=urls)
#             yield item
