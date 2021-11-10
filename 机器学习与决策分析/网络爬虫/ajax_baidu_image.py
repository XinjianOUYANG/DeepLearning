import requests
import json
import os
import time

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}


def download_images(start_url, img_format, max_value, dir_name):
    current_value = 0
    image_index = 1
    while current_value < max_value:
        current_url = start_url.format(current_value)
        result = requests.get(current_url, headers=headers)
        json_str = result.text
        imageResult = json.loads(json_str) # 将json字符串形式转化为dict类型
        data = imageResult['data'] # dict类型， 网页数据在’data‘属性中
        for record in data:
            url = record.get('middleURL')
            if url != None:
                print('正在下载图片：',url)
                # record是dict类型，这里不用record['middleURL']是因为每一页中的最后一个data是空的，他没有'middleURL'，
                # 如果用record.get('middleURL') 则返回None
                r = requests.get(url, headers=headers)
                filename = dir_name + '/' + str(image_index).zfill(10) \
                           + '.' + img_format  # zfill()方法返回指定长度的字符串，原字符串右对齐，前面填充0。
                with open(filename, 'wb') as f:
                    f.write(r.content)
                image_index += 1
                time.sleep(2)
        current_value += 30
    print('图像下载完成')




if __name__ == '__main__':
    start_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com' \
                '&logid=10673237574252885038&ipn=rj&ct=201326592&is=&fp=' \
                'result&queryWord=%E7%BB%9D%E5%9C%B0%E6%B1%82%E7%94%9F&cl=2' \
                '&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=' \
                '&copyright=&word=%E7%BB%9D%E5%9C%B0%E6%B1%82%E7%94%9F&s=&se=' \
                '&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=' \
                '&force=&pn={}&rn=30&gsm=1e&1616817928578='
    dir_name = "绝地求生"
    print('图像文件将保存在', dir_name, '目录中')
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    max_value = 120
    img_format = 'png'
    download_images(start_url, img_format, max_value, dir_name)
