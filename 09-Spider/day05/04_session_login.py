import requests
from lxml import etree

# 1.先post（把用户名和密码post到一个地址中）
post_url = 'http://www.renren.com/PLogin.do'
post_data = {
    'email':'18857282845',
    'password':'18857282845'
}
headers = {
    'User-Agent':'Mozilla/5.0',
    'Referer':'http://www.renren.com/SysHome.do',
}
# 实例化session对象
session = requests.session()
session.post(url=post_url,data=post_data,headers=headers)

# 2.再get（访问需要登录后才能访问的页面）
url = ''
html = session.get(url,headers=headers).text