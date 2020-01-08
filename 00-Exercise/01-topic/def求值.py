def myfun(a,b):
    print('最大',max(a,b))
    print('和',a + b)
    print('积',a * b)
    i = a
    while i < b:
        if i % 2 == 0:
            print('偶数是',i,end=' ')
        i += 1
    print()
myfun(10,20)  