from itemadapter import ItemAdapter
import os
from urllib import request


class PorschePipeline:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category = item['category']
        urls = item['image_urls']

        category_path = os.path.join(self.path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        for url in urls:
            image_name = url.split('_')[-1]
            request.urlretrieve(url, os.path.join(category_path, image_name))

        return item


