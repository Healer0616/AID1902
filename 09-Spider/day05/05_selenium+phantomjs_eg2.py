# 导入selenium中webdriver接口
from selenium import webdriver
import time

# 创建浏览器对象
browser = webdriver.Chrome()
# 打开百度
browser.get('http://www.baidu.com/')
# 找到搜索框，发送文本
text = browser.find_element_by_xpath('//*[@id="kw"]')
text.send_keys('李易峰')
# 找到 百度一下 按钮 点击
button = browser.find_element_by_xpath('//*[@id="su"]')
button.click()
time.sleep(2)
# 截图
browser.save_screenshot('李易峰.jpg')