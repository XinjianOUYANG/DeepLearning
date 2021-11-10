import requests

response = requests.get('https://www.baidu.com')
if response.status_code == 200:
    print('获得正常响应')

for key, value in response.request.headers.items():
    print(key, ':', value)
