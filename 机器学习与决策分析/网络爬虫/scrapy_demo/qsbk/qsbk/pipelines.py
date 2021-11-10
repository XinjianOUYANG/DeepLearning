# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


######### 第一种方式：按照传统字典形式数据格式进行写入 ################
# import json

# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open("duanzi.json", "w", encoding="utf-8")
#
#
#     def open_spider(self, spider):
#         print("这是爬虫开始了...")
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         pring("这是爬虫结束了...")

# ######### 第一种方式：按照JsonItemExporter进行写入 ################
# # 此种方式在执行exporter.export_item()时，是先把所有item数据先存在一个列表中，
# # 然后在执行exporter.finish_exporting()时再把数据统一以列表形式写入，如果数据
# # 量较大时，占内存空间
# from scrapy.exporters import JsonItemExporter
# class QsbkPipeline:
#     def __init__(self):
#         self.fp = open("duanzi.json", "wb")
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#
#     def open_spider(self, spider):
#         print("这是爬虫开始了...")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         pring("这是爬虫结束了...")


######### 第三种方式： 按照JsonLinesItemExporter写入 ################
# 此种方式在执行时是将数据一条一条写入的，不耗内存；而且不需要start_exporting和finish_exporting操作


from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline:
    def __init__(self):
        self.fp = open("duanzi.json", "wb")
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print("这是爬虫开始了...")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        pring("这是爬虫结束了...")


######  当然，scrapy.exporters库中还有csv等格式数据的导入方式