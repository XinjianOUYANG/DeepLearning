from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://171.35.213.97:9999")

driver_path = './chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get('http://httpbin.org/ip')


