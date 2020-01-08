L = []
while True:
    a = input("请输入：")
    if not a:
        break
    
    L.append(a)

s = set(L)
print("输入了%d种" % len(s))
L2 = []
for x in L:
    if x not in L2:
        L2.append(x)
for x in L2:
    print(x)