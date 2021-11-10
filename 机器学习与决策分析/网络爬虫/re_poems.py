import re
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Referer': 'https://www.gushiwen.cn/'
}

def parse_page(url):
    response = requests.get(url, headers= headers)
    text = response.text
    # 这里千万不要忘记加上`re.DOTALL`这个参数，这个参数意味着.能够匹配包括换行\n在内的任意字符，
    # 如果不加上这个参数，就会匹配不到
    titles = re.findall(r'<div class="cont">.*?<p>.*?<a.*?<b>(.*?)</b>', text, re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?</a>.*?<a.*?>〔(.*?)〕</a>', text, re.DOTALL)
    contents = re.findall(r'<div class="contson".*?>(.*?).</div>', text, re.DOTALL)
    poems = []
    for content in contents:
        poem = re.sub('<.*?>', '', content) # 将内容中的标签<>符号去掉
        poem = poem.strip() # 将两端的空白去掉
        poems.append(poem)

    poem_infos = []
    for title, author, dynasty, poem in zip(titles, authors, dynasties, poems):
        poem_info = {
            'title': title,
            'author': author,
            'dynasty': dynasty,
            'poem': poem
        }
        poem_infos.append(poem_info)
        print(poem_info)
    return poem_infos

if __name__ == '__main__':
    urls = ['https://www.gushiwen.cn/default_{}.aspx'.format(str(i)) for i in range(1,11)]
    poem_total_infos = []
    for url in urls:
        poem_infos = parse_page(url)
        poem_total_infos = poem_total_infos + poem_infos
        time.sleep(1)

