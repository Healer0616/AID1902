import requests
url = 'http://www.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0'
}

res = requests.get(url,headers=headers)
# 显示字符编码
res.encoding = 'utf-8'

print(res.text)