# -*- coding: utf-8 -*- 
# @Time    : 2020/12/31 4:52 下午
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : baidulogin.py
# @Software: PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 添加Cookie
driver.add_cookie({'name': 'BAIDUID', 'value': '66DD2D371D19A91CDFF5C032DF4581B7:FG=1'})
driver.add_cookie({'name': 'BDUSS',
                   'value': 'Jyai01LTlpV0h-NElhb29jb3kzZTdUfmRza1JFMFVPcmF1U0VraFY1VWRIeFZnSVFBQUFBJCQAAAAAAAAAAAEAAAA7KD5lcXoxMjN6eHYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB2S7V8dku1fVE'})

# 刷新页面
driver.refresh()

# 获取登录用户名并打印
username = driver.find_element_by_class_name("user-name").text
print(username)

# 关闭浏览器
driver.quit()
