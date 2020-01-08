

from socket import *

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,True)

#选择接收地址
s.bind(('0.0.0.0',9999))

while True:
    msg,addr = s.recvfrom(1024)
    print(msg.decode())

"""
请求行：具体的请求类别和请求内容
格式： GET        /       HTTP/1.1
     请求类别   请求内容    协议版本
请求类别：每个请求类别表达不同的请求方式和行为
  GET：获取网络资源
  POST：提交一定的信息，得到反馈
  HEAD：只获取网络资源响应头
  PUT：更新服务器资源
  DELETE：删除服务器资源
  CONNECT：
  TRACE：测试
  OPTIONS：获取服务器性能信息

请求头：对请求的进一步描述和解释
  Accept-Encoding：gzip

空行

请求体：请求参数或者提交内容
"""