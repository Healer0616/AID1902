# -*- coding: utf-8 -*- 
# @Time    : 2020/1/16 下午8:03
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : get_token.py
# @Software: PyCharm


import requests, json

url = "https://manage.i31.com/elevator/maintain/login/by/pwd"
headers = {"Content-Type": "application/json;charset=UTF-8", "token": "9c3d92e5a7e7aae78726fee0c40f7956"}
data = {
    "loginName": "adminrenbao",
    "pwd": "e10adc3949ba59abbe56e057f20f883e"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)

# 获取token
a_token = response.json()['data']['token']

url_get = ("https://manage.i31.com/elevator/maintain/user/my/menu")
headers = {"Content-Type": "application/json;charset=UTF-8", "token": a_token}
r = requests.get(url_get, headers=headers)
print(r.text)
