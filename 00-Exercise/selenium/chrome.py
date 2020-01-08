from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# 定义浏览器
browser = webdriver.Chrome()
try:
    browser.get("http://www.baidu.com")
    input = browser.find_element_by_id("kw")
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()




# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# print(browser.page_source)
# browser.close()




# 前进后退

# browser = webdriver.Chrome()
# browser.get("https://www.baidu.com/")
# browser.get("https://www.taobao.com/")
# browser.get("https://www.douyu.com/")
# browser.get("http://www.tieba.com/")
# # 后退一步
# browser.back()
# time.sleep(3)
# # 前进一步
# browser.forward()
# browser.close()
