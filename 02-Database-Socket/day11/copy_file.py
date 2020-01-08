from multiprocessing import Process
import os

# 变量绑定文件名
filename = "timg.jpg"
# 获取文件大小
size = os.path.getsize(filename)

f = open(filename,"rb")

# 复制上半部分
def new_up():
    # r = open(filename,"rb")
    n = size // 2
    with open("upimg.jpg","wb") as fw:
        fw.write(f.read(n))
    # f.close()

# 复制下半部分
def new_dowm():
    # r = open(filename,"rb")
    f.seek(size//2,0) # 移动文件偏移量
    with open("downimg.jpg","wb") as fw:
        fw.write(f.read())
    # f.close()

# 创建进程
p1 = Process(target = new_up)
p2 = Process(target = new_dowm)

# 启动进程
p1.start()
p2.start()

# 回收进程
p1.join()
p2.join()

f.close()