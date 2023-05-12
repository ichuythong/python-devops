from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('http://127.0.0.1:5000')
driver.maximize_window()
time.sleep(3)
print('hi')
task = driver.find_element_by_xpath('/html/body/div/form/div/input')
task.send_keys('Test')
print('world')
add = driver.find_element_by_xpath('/html/body/div/form/button')
add.click()
time.sleep(3)
print('www')
update = driver.find_element.by_xpath('/html/body/div/div/a[1]')
update.click()
print('yyyy')
delete = driver.find_element_by_xpath('/html/body/div/div/a[2]')
delete.click()
time.sleep(3)
driver.close()
driver.quit()

#list_task = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
list_task = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
list_task.get('http://127.0.0.1:5000')
time.sleep(3)
driver.close()
driver.quit()

