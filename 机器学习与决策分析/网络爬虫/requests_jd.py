import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.114 Safari/537.36'
}
response = requests.get('https://www.jd.com', headers=headers)
for key, value in response.request.headers.items():
    print(key, ':', value)

print(response.text)
print('=' * 50)
print(response.content)
print('=' * 50)
print(response.encoding)