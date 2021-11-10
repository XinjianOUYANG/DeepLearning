from selenium import webdriver
import time

driver_path = './chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.jd.com")
time.sleep(3)
driver.execute_script("window.open('https://www.baidu.com')")
print(driver.current_url)
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
time.sleep(3)

driver.execute_script("window.open('https://www.suning.com')")
time.sleep(3)
driver.close()
time.sleep(3)
driver.quit()

# 在浏览器中打开一个新的窗口
# 虽然在浏览器窗口显式已经切换到了新的页面，但是driver中还没有切换。
# 如果想要在代码中切换到新的页面，并且做一些爬虫，就应该使用driver.switch_to.window
# 来切换到指定的窗口。