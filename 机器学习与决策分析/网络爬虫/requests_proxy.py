import requests
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) '
                'Chrome/88.0.4324.190 Safari/537.36',
  'Refer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

proxies = {
    "http": "http://12.34.56.79:9527",
    "https": "https://12.34.56.79:9527"
}

url = 'http://httpbin.org/ip'
response = requests.get(url, proxies=proxies, headers=headers)
print(response.text)

