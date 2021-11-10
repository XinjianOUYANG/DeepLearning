import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
}

url = 'https://www.xfz.cn/api/website/articles/?p=2&n=20&type='

response = requests.get(url, headers=headers)
res_dic = response.json()
print(type(res_dic))
print(res_dic['data'][0])


