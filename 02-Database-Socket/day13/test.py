# 计算密集
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# IO 密集
def io():
    write()
    read()

def write():
    f = open("test","w")
    for i in range(1700000):
        f.write("hello world\n")
    f.close()

def read():
    f = open("test")
    f.readlines()
    f.close()

# 结论：在无阻塞情况下，多线程程序运行效率和单线程几乎相近，而多进程可以有效的提高程序的运行效率