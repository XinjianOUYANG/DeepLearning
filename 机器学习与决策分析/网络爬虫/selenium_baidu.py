# from selenium import webdriver
#
# driver_path = './chromedriver_win32/chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
# print(driver.page_source)


from selenium import webdriver
import time

driver_path = './chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('selenium网络爬虫')
BtnTag = driver.find_element_by_id('su')
BtnTag.click()
time.sleep(3)
inputTag.clear()

inputTag = driver.find_element_by_name('wd')
inputTag.send_keys('python')
BtnTag = driver.find_element_by_id('su')
BtnTag.click()
time.sleep(3)
inputTag.clear()

inputTag = driver.find_element_by_class_name('s_ipt')
inputTag.send_keys('机器学习')
BtnTag = driver.find_element_by_id('su')
BtnTag.click()
time.sleep(3)
inputTag.clear()

inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
inputTag.send_keys('深度学习')
BtnTag = driver.find_element_by_id('su')
BtnTag.click()
time.sleep(3)
inputTag.clear()

inputTag = driver.find_element_by_css_selector('input#kw')
inputTag.send_keys('强化学习')
BtnTag = driver.find_element_by_id('su')
BtnTag.click()
time.sleep(3)
inputTag.clear()


# 1. 如果只是想要解析网页中的数据，那么推荐将网页源代码扔给lxml来解析，
# 因为lxml底层使用的是C语言，所以解析效率会更高
# 2. 如果想要对元素进行一些操作，比如给一个文本框输入值，或是点击某个按钮，则
# 必须使用selenium给我们提供查找元素的方法