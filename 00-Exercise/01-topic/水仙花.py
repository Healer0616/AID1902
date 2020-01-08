for x in range(100,1000):
    bai = x // 100
    shi = x % 100 //10
    ge = x % 100 % 10
    if x == bai ** 3 + shi ** 3 + ge ** 3:
        print(x)
    