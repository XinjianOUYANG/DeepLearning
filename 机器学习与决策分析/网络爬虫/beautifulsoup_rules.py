from bs4 import BeautifulSoup

text = '''
<html>
    <body>
        <div>
            <ul>
                <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
                <li id='first' class="item1"><a href="https://www.jd.com"> 京东商城</a></li>
                <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
                <li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
                <li class="item5"><a href="https://www.google.com">谷歌</a></li>
            </ul>
        </div>
    </body>
</html>
'''
soup = BeautifulSoup(text, 'lxml')
print(type(soup))
print(soup)
print('=' * 50)
print(soup.prettify())
print('=' * 50)

liList = soup.find_all('li')
print(liList)
print('=' * 50)

liList = soup.find_all('li', limit=2)
print(liList)
print('=' * 50)

# 尽管ul节点只有一个，但find_all依然返回一个列表
ulList = soup.find_all('ul')
print(ulList)
print('=' * 50)

# 获取class为item1且id为first的li标签
liList1 = soup.find_all('li', id='first', class_='item1')
print(liList1)
print('=' * 50)
liList2 = soup.find_all('li', attrs={'id': 'first', 'class': 'item1'})
print(liList2)
print('=' * 50)

li1 = soup.find('li')
print(li1)
print('=' * 50)
li2 = soup.find('li', id='first', class_="item1")
print(li2)
print('=' * 50)
li3 = soup.find('li', attrs={'class': 'item4', 'value': '1234'})
print(li3)
print('=' * 50)


aList= soup.find_all('a')
for a in aList:
    href = a['href']
    print(href)
print('=' * 50)





text = '''
<html>
    <body>
        <div>
            <ul>
                <li class="item1"><a href="https://geekori.com">
                    geekori.com  西安交通大学  
                      </a></li>
                <li id='first' class="item1"><a href="https://www.jd.com"> 京东商城
                </a>
                兴庆校区
                </li>
                <li class="item3"><a id='first' href="https://www.taobao.com"> 淘宝 </a></li>
                <li class="item4" value="1234"><a href="https://www.microsoft.com"> 微软 </a></li>
                <li class="item5"><a href="https://www.google.com">
                    谷歌
                </a></li>
            </ul>
        </div>
    </body>
</html>
'''
# 获取非标签文本
soup = BeautifulSoup(text, 'lxml')
liList = soup.find_all('li')
print(liList[0].string)
print('=' * 50)
print(liList[1].string)
print('=' * 50)
print(list(liList[1].strings))
print('=' * 50)
print(list(soup.stripped_strings))
print('=' * 50)
print(liList[1].get_text())
print('=' * 50)


# 运用select方法获取节点
soup = BeautifulSoup(text, 'lxml')
aList = soup.select('a')
for a in aList:
    print(a)
print('=' * 50)
liList2 = soup.select('.item3')
print(liList2)
print('=' * 50)
idFirstList3 = soup.select('#first')
print(idFirstList3)
print('=' * 50)
a_idFirstList4 = soup.select('a#first')
print(a_idFirstList4)
print('=' * 50)
a_classItem5List5 = soup.select('li.item5>a')
print(a_classItem5List5)
print('=' * 50)
li_value1234List6 = soup.select('li[value="1234"]')
print(li_value1234List6)
