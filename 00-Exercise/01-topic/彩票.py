i = 1
L = []
while True:
    if i < 7:
        num = int(input("请输入%d"%(i)))
        if 1 <= num <= 33:
            if num not in L:
                i += 1
                L.append(num)
            else:
                print("重新输入")
        else:
            print("超出范围，重新输入")
    L.sort()
    if i == 7:
        num = int(input("请输入7号"))
        if 1 <= num <= 16:
            L.append(num)
            break
        else:
            print("超出范围，重新输入")
print(L)

        


