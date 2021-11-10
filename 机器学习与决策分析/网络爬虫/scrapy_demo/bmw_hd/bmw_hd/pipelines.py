# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import os
from bmw_hd import settings

class BMWImagesPipeline(ImagesPipeline):
    # 这个方法是在发送请求下载请求之前调用，其实这个方法本身就是去发送下载请求的
    def get_media_requests(self, item, info):
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    # 这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
    def file_path(self, request, response=None, info=None, item=None):
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)
        return image_path
