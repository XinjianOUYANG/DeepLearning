import requests
from lxml import etree
import random
import time
import json

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Referer': 'https://www.xfz.cn/',
  'Cookie': 'csrftoken=dKp8h7RFCGrtgmHUKHhZDfUwIuSxvUz3; Hm_lvt_d8ac74031a6495039421daa89265b01d=1616404252; Hm_lpvt_d8ac74031a6495039421daa89265b01d=1616404684'
}


def parse_page(url):
    response = requests.get(url, headers=headers)
    response_json = response.json()
    response_json_data_list = response_json['data']
    ids = []
    for response_json_data in response_json_data_list:
        id = response_json_data['uid']
        ids.append(id)
    return ids


def parse_details(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)

    title = html.xpath('//h1[@class="title"]/text()')[0]
    author = html.xpath('//span[@class="author-name"]/text()')[0]
    pub_time = html.xpath('//span[@class="time"]/text()')[0]
    content_lead = html.xpath('//div[@class="content-lead"]/text()')[0].strip()
    content = html.xpath('//div[@class="content-detail"]//span/text()')

    content = ''.join(content)
    img_urls = html.xpath('//div[@class="content-detail"]//img/@src')
    article_detail = {
        'title': title,
        'author': author,
        'pub_time': pub_time,
        'content_lead': content_lead,
        'content': content,
        'img_urls': img_urls,
    }
    return article_detail


if __name__ == '__main__':
    BASE_DETAIL_URL = 'https://www.xfz.cn/post/{}.html'
    urls = ['https://www.xfz.cn/api/website/articles/?p={}&n=20&type='.format(str(i))
            for i in range(1, 2)]
    count = 0
    with open('xfz_articles.json', 'w', encoding='utf-8') as fp:
        article_details = []
        for url in urls:
            ids = parse_page(url)
            time.sleep(random.choice(range(1, 5)))
            detail_urls = list(map(lambda x: BASE_DETAIL_URL.format(x), ids))
            for detail_url in detail_urls:
                article_detail = parse_details(detail_url)
                article_details.append(article_detail)
                count += 1
                print('第%d条记录完成了' % count)
                time.sleep(random.choice(range(1, 5)))
        json.dump(article_details, fp, ensure_ascii=False)
        print('文件保存成功！')

