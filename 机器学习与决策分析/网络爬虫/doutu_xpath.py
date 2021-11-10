import requests
from lxml import etree
import os
from urllib import request
import re
import time
import random

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Referer': 'https://www.doutula.com/photo/list/?page=2'
}

def parse_page(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)

    div = html.xpath('//div[@class="page-content text-center"]')[0]
    aList = div.xpath('.//a')

    if not os.path.exists('doutu_images'):
        os.mkdir('doutu_images')

    index = 0
    for a in aList:
        # print(etree.tostring(a, encoding='utf-8').decode('utf-8'))
        img_url = a.xpath('./img[@class!="gif"]/@data-original')[0]
        name = a.xpath('./p/text()')
        if len(name) ==0:
            index += 1
            name = str(index)
        else:
            name = name[0]

        # 请注意，在character类的方括号内，许多转义是不必要的，而在character类之外则是必要的。例如，正则表达式[\.]与[.]相同
        name = re.sub(r'[！!?？。./|]+', '', name)
        img_form = img_url.split('.')[-1]
        store_path = 'doutu_images/' + name + '.' + img_form
        request.urlretrieve(img_url, store_path)


if __name__ == '__main__':
    urls = ['https://www.doutula.com/photo/list/?page={}'.format(str(i)) for i in range(1,11)]
    for index, url in enumerate(urls):
        parse_page(url)
        print("第{}页下载成功".format(str(index)))
        time.sleep(random.choice(range(1,5)))