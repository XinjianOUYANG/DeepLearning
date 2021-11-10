import requests
data = {
    'name': 'Bill',
    'country': '中国',
    'age': 20
}

response = requests.post('http://httpbin.org/post', data=data)
print(response.text)
print('=' * 50)
print(response.content)
print('=' * 50)
print(response.content.decode('unicode_escape'))
print('=' * 50)
print(response.json())
print('=' * 50)
print(response.json()['form']['country'])




