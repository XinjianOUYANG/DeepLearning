import requests
from lxml import etree

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'Referer': 'https://movie.douban.com/cinema/nowplaying/xian/'
}

url = 'https://movie.douban.com/cinema/nowplaying/xian/'
response = requests.get(url, headers=headers)

text = response.text
html = etree.HTML(text)

liList = html.xpath('//div[@id="nowplaying"]//ul[@class="lists"]/li')

movies = []
for li in liList:
    title = li.xpath('./@data-title')[0]
    score = li.xpath('./@data-score')[0]
    data_release = li.xpath('./@data-release')[0]
    actors = li.xpath('./@data-actors')[0]
    director = li.xpath('./@data-director')[0]
    post = li.xpath('.//li[@class="poster"]//img/@src')[0]
    movie = {
        'title': title,
        'score': score,
        'data_release': data_release,
        'actors': actors,
        'director': director,
        'post': post,
    }
    movies.append(movie)
    print(movie)

print(len(movies))
