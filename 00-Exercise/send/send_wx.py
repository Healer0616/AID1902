# -*- coding: utf-8 -*- 
# @Time    : 2020/1/14 下午11:02
# @Author  : Healer
# @Email   : healer0616@126.com
# @File    : send_wx.py
# @Software: PyCharm

import itchat

# 登录微信　　括号中的参数如果不写的话　那么就不会保留最近的登录状态
# 从而每次运行程序都要扫描二维码
itchat.auto_login(hotReload=True)
# 计数器开关
cnt = 0
remarkname = input("请输入您要轰炸的人:")# 查找对应好友(你给他的备注名)
try:
    # 　这句话是获取你的好友列表并从中找到你要轰炸的人
    name = itchat.search_friends(remarkname)[0]['UserName']
    # 　我在这里限制了次数，就是发送三次，如果你想无限轰炸,就将3改成大一点的数字
    # 　建议将 cnt < 3 改成　199　就可以了　，太高了容易造成发送管道阻塞,
    # 那样的话就需要半个多小时才能和朋友聊天
    while cnt < 3:
        # 　每执行依次，都会趋向于结束
        cnt += 1
        # 　发送文字消息
        itchat.send_msg("本消息为Python程序自动发送，如有打扰望见谅", name)
        # 　发送图片
        # itchat.send_image("/home/tarena/project/test/ .png", name)
        # 发送文件
        # itchat.send_file("/home/tarena/project/js/day02.txt", name)
except IndexError as i:
    print("未搜索到 %s" % remarkname)
except Exception as e:
    print(e)
