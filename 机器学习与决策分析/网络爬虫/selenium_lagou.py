import csv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import re
import random
import time

class LagouSpider(object):
    driver_path = 'chromedriver_win32/chromedriver.exe'
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords='

    def run(self):
        self.driver.get(self.url)  # 打开网页
        positions = []
        while True:
            WebDriverWait(driver=self.driver, timeout=300).until(
                EC.presence_of_element_located(
            (By.XPATH, '//div[@class="pager_container"]/span[last()]')
                )
            )
            source  = self.driver.page_source
            positions_one_page = self.parse_list_page(source)
            positions += positions_one_page

            next_btn = self.driver.find_element_by_xpath\
                ('//div[@class="pager_container"]/span[last()]')              # 获得`下一步`的按钮
            if 'pager_next_disabled' not in next_btn.get_attribute('class'):   # 如果`下一步`按钮能够点击
                next_btn.click()                                               # 则点击下一页
                time.sleep(random.choice(range(2,10)))
            else:
                break
        return positions

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath('//a[@class="position_link"]/@href')
        positions_one_page = []
        for link in links:
            position = self.request_detail_page(link)
            positions_one_page.append(position)
            time.sleep(random.choice(range(2,10)))
        return positions_one_page


    def request_detail_page(self, url):
        self.driver.execute_script('window.open("%s")' % url)             # 在当前浏览器窗口打开新的一页
        self.driver.switch_to.window(self.driver.window_handles[1])       # 切换到新打开的这页详情页
        WebDriverWait(driver=self.driver, timeout=300).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[@class="position-head-wrap-name"]')
            )
        )
        source = self.driver.page_source
        position = self.parse_detail_page(source)
        self.driver.close()                                                # 关闭当前这个详情页
        self.driver.switch_to.window(self.driver.window_handles[0])       # 继续切换回职位列表页
        return position

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        position_name = html.xpath('//span[@class="position-head-wrap-name"]/text()')[0]
        company_name = html.xpath('//em[@class="fl-cn"]/text()')[0].strip()
        job_request_spans = html.xpath('//dd[@class="job_request"]//span//text()')
        salary = job_request_spans[0].strip()
        city = re.sub(r'[/\s]','',job_request_spans[1])
        work_years = re.sub(r'[/\s]','',job_request_spans[2])
        education = re.sub(r'[/\s]','',job_request_spans[3])
        status = re.sub(r'[/\s]','',job_request_spans[4])
        job_detail = html.xpath('//div[@class="job-detail"]//text()')
        job_detail = ''.join(job_detail).strip()
        position = {
            'position_name': position_name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': education,
            'status': status,
            'job_detail': job_detail
        }
        print(position)
        print('=' * 50)
        return position


if __name__ == '__main__':
    spider = LagouSpider()
    positions = spider.run()
    headers = list(positions[0].keys())

    # headers = ['position_name', 'company_name', 'salary',  'city',
    #         'work_years', 'education', 'status', 'job_detail']
    with open('lagou_postions.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(positions)



