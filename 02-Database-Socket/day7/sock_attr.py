

#套接字属性演示 理解

from socket import * 

#创建套接字对象
s = socket()

#设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

print(s.family) #地址类型    AddressFamily.AF_INET
print(s.type) #套接字类型    SocketKind.SOCK_STREAM

s.bind(('0.0.0.0',8888))
print(s.getsockname()) #绑定地址    ('176.23.5.149',8888)

print(s.fileno()) #获取文件描述符    3
  #文件描述符：系统中每一个IO操作都会分配一个整数作为编号，该整数即这个IO的文件描述符
  #特点：每个IO的文件描述符不会重复

s.listen(3)
c,addr = s.accept()
print(c.getpeername()) #获取c连接的客户端地址    ('127.0.0.1', 35264)

# setsockopt(level,option,value)
#功能：设置套接字选项
#参数：level 选项类别  SOL_SOCKET
#     option 具体选项内容
#     value 选项值

# UDP套接字广播
# 广播定义：一端发送，多端接收
# 广播地址：每个网段内的最大地址，向该地址发送则网段内所有的主机都能接收

