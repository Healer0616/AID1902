n = int(input("请输入树干的高度"))
for i in range(1,(n+1)):
    k = (n - i)
    print(' ' * k + '*' * (i * 2 - 1))
for i in range(1 , n + 1):
    print(' ' * (n - 1) + '*')

    