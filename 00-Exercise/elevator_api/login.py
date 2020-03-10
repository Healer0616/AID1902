# -*- coding: utf-8 -*- 
# @Time    : 2020/1/16 下午8:47
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : login.py
# @Software: PyCharm

import requests, json


class Elevator_login(object):
    def __init__(self, url, headers, data):
        self.url = url
        self.headers = headers
        self.data = data

    def get_token(self):
        url = self.url + "/login/by/pwd"
        headers = self.headers
        data = self.data
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response.json()['data']['token']

    def get_menu(self):
        # a_token = Elevator_login.get_token(self).response.json()['data']['token']
        # payload = {}
        token = self.get_token()
        headers = {
            'token': token
        }
        url = self.url + "/user/my/menu"
        # headers = {"Content-Type": "application/json;charset=UTF-8", "token": a_token}
        response = requests.get(url, headers=headers)
        return response.text


if __name__ == '__main__':
    url = "https://manage.i31.com/elevator/maintain"
    headers = {
        'Content-Type': 'application/json',
        'token': '',
        'Authorization': 'Bearer 637703e790a2066f82d198087808c658'
    }
    data = {
        "loginName": "adminrenbao",
        "pwd": "e10adc3949ba59abbe56e057f20f883e"
    }
    e = Elevator_login(url, headers, data)
    print(e.get_token())
    print(e.get_menu())
