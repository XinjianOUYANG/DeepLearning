from lxml import etree

text = '''
<html>
    <head>
        <meta charset="UTF-8">
        <li class="item2"><a href="https://www.taobao.com">咸鱼</a></li>
        <title>XPath演示</title>
    </head>
    <body>
        <div>
            <ul>
                <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
                <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
                <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
                <li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
                <li class="item5"><a href="https://www.google.com">谷歌</a></li>
'''
html = etree.HTML(text)
print(etree.tostring(html, encoding='utf-8').decode('utf-8'))


headTags = html.xpath('head')
print(etree.tostring(headTags[0], encoding='utf-8').decode('utf-8'))

bodyTags = html.xpath('body')
print(etree.tostring(bodyTags[0], encoding='utf-8').decode('utf-8'))

divsTags = html.xpath('body/div')
print(etree.tostring(divsTags[0], encoding='utf-8').decode('utf-8'))
divsTags = html.xpath('//div')
print(etree.tostring(divsTags[0], encoding='utf-8').decode('utf-8'))

liTags = html.xpath('body/div/ul/li')
liTags = html.xpath('//div/ul/li')
liTags = html.xpath('//ul/li')
liTags = html.xpath('//li')
for liTag in liTags:
    print(etree.tostring(liTag, encoding='utf-8').decode('utf-8'))



liTag = html.xpath('//ul/li[1]')
print(etree.tostring(liTag[0], encoding='utf-8').decode('utf-8'))

liTag = html.xpath('//ul/li[last()]')
print(etree.tostring(liTag[0], encoding='utf-8').decode('utf-8'))

liTags = html.xpath('//ul/li[position()>3]')
for liTag in liTags:
    print(etree.tostring(liTag, encoding='utf-8').decode('utf-8'))


liTag = html.xpath('//ul/li[@class="item2"]')
print(etree.tostring(liTag[0], encoding='utf-8').decode('utf-8'))

href = html.xpath('//ul/li[@class="item2"]//@href')
print(href)

href = html.xpath('//ul/li[@class="item2"]//text()')
print(href[0].strip())

ulTag = html.xpath('//ul')[0]
aTag1 = ulTag.xpath('//a')[0]
print(etree.tostring(aTag1, encoding='utf-8').decode('utf-8'))
print('=' * 40)
aTag2 = ulTag.xpath('.//a')[0]
print(etree.tostring(aTag2, encoding='utf-8').decode('utf-8'))




