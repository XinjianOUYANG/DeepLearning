from bs4 import BeautifulSoup
import requests
import time
import random

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
  'Cookie': 'abtest_ABTest4SearchDate=b; xzuuid=d436de45; sajssdk_2015_cross_new_user=1; distinctId=179089d4828563-0d837ffcd684bf-c3f3568-1508512-179089d4829b39; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179089d4828563-0d837ffcd684bf-c3f3568-1508512-179089d4829b39%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179089d481d375-03cc4a7386a92d-c3f3568-1508512-179089d481e4ae%22%7D; Hm_lvt_92e8bc890f374994dd570aa15afc99e1=1619347196; wttXMuWwbC=30c27a8bea77448f133a773f5353a14dbe5988dc; ATNgmRNkrw=1619348857; Hm_lpvt_92e8bc890f374994dd570aa15afc99e1=1619348859',
   'Referer': 'https://xa.xiaozhu.com/search-duanzufang-p2-0/',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1'
}

# 抓取一页小猪网西安地区房源的HTML代码，并得到本页所有房源的主页
def get_links(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # 提取class属性值为resule_img_a的所有a节点
    aTags = soup.find_all('a', class_='resule_img_a')
    # 每一个房源详细信息链接在a节点中的href属性中
    for number, aTag in enumerate(aTags):
        href = aTag['href']
        house_info = parse_details(href)
        time.sleep(random.choice(range(1,5)))
        print(number, house_info)

# 从房源主页的HTML代码中提取标题、地址、价格等信息，并以字典形式返回这些信息
def parse_details(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.select('div.pho_info>h4>em')[0].string.strip()
    address = soup.select('span.pr5')[0].string.strip()
    price = soup.select('div.day_l>span')[0].string.strip()
    image_url = soup.select('img#curBigImage')[0]['src']
    name = soup.select('a.lorder_name')[0].string.strip()
    female_tag = soup.select('div.member_ico1')
    male_tag = soup.select('div.member_ico')
    if len(female_tag) != 0:
        sex = '女'
    elif len(male_tag) != 0:
        sex = '男'
    else:
        sex = '未知'
    score_tag = soup.select('span.x_textscore')
    if len(score_tag) !=0:
        score = list(soup.select('span.x_textscore')[0].strings)[0]
    else:
        score = '没有评分'
    info = {
        'title': title,
        'address': address,
        'price': price,
        'image_url': image_url,
        'name': name,
        'sex': sex,
        'score': score
    }
    return info

    # div = soup.find('div', class_='pho_info')
    # h4 = div.find('h4')
    # title = h4.find('em').string.strip()
    # div_day_l = soup.find(class_='day_l')
    # price = div_day_l.find('span').string.strip()
    # image_url = soup.find('img', id='curBigImage')['src']
    # name = soup.find('a', class_='lorder_name').string
    # female_tag = soup.find('div', class_='member_ico1')
    # male_tag = soup.find('div', class_='member_ico')


if __name__ == '__main__':
    single_url = 'https://xa.xiaozhu.com/'
    get_links(single_url)





