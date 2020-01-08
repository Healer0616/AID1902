w = int(input("请输入三角形的宽度"))
i = 1
while i <= w :
    k = w - i 
    print(' ' * k + '*' * i)
    i += 1
print('--------第二个三角形--------')
i = w 
while i > 0:
    k = w - i
    print(' ' * k + '*' * i)
    i -= 1
print('--------第三个三角形--------')
i = w
while i > 0:
    print('*' * i)
    i -= 1