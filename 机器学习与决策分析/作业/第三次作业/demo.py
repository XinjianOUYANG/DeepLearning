#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   demo.py
@Time    :   2021/10/16 13:09
@Author  :   Jinnan Huang 
@Contact :   jinnan_huang@stu.xjtu.edu.cn
@Desc    :   None
"""
import requests
import re


def get_page():
    # 获取第一页的所有新闻的URL，翻页就是改变这个URL的构造方式，有规律，大家自己研究一下
    url = "http://news.xjtu.edu.cn/ywjj.htm"
    headers = {
        'Proxy-Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://news.xjtu.edu.cn/',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cookie': 'JSESSIONID=9E4AE5CE70EB42729F6042EA199D32D3'
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    res_text = response.text

    # 总共有多少页
    page_range = re.search(r'\u5171([0-9]+)\u9875', response.text)[1]

    # 第一页中所有的新闻链接列表
    ref_list = re.findall(r'<a href=["]info/(.+?)["]', res_text)

    # 构造新闻的链接，然后爬取新闻内容，这里以一则新闻为例
    for ref in ref_list:
        url = f'http://news.xjtu.edu.cn/info/{ref}'
        page_content = requests.get(url=url)
        page_content.encoding = 'utf-8'
        page_content_text = page_content.text  # 包含新闻正文的HTML字符串
        print(page_content_text)
        break

    # 使用Xpath, bs4, re等包提取新闻正文，这里就不写了，大家自己参考API文档


if __name__ == '__main__':
    get_page()
