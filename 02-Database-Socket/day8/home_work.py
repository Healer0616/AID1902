

from select import select
from socket import *
import sys
from time import ctime

#日志文件
f = open('log.txt','a')

#创建套接字
s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#添加到关注列表
rlist = [s,sys.stdin]
wlist = []
xlist = []

while True:
    #监控IO
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        #s就绪说明有客户端连接
        if r is s:
            c,addr = r.accept()
            # print("Connect from",addr)
            #将客户端套接字加入关注列表
            rlist.append(c)
        #如果是c就绪则表示对应的客户端发送消息
        elif r is sys.stdin:
            name = "Server"
            time = ctime()
            msg = r.readline()
            f.write("%s %s %s\n"%(name,time,msg))
            f.flush() #清缓存
        else:
            addr = r.getpeername()
            time = ctime()
            msg = r.recv(1024).decode()
            f.write("%s %s %s\n"%(addr,time,msg))
f.close()
s.close()

    # for w in ws:
    #     w.send(b"OK")
    #     wlist.remove(w)

    # for x in xs:
    #     pass
