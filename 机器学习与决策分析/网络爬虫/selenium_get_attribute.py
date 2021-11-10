from selenium import webdriver

driver_path = './chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
print(inputTag.get_attribute('type'))
print(inputTag.get_attribute('class'))
print(inputTag.get_attribute('name'))
print(inputTag.get_attribute('id'))

