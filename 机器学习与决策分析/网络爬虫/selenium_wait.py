# 隐式等待
from selenium import webdriver

driver_path = './chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://lian.xiniu.com/')
driver.implicitly_wait(10) # 在10秒后才会执行下一步
element = driver.find_element_by_name('UserName')
print(element)



# 显式等待
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = './chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://lian.xiniu.com/')
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, 'UserName'))
)
print(element)


