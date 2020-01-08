L = []
while True:
    a = input("请输入姓名：")
    if a == "":
        break
    
    b = input("请输入年龄：")
    c = input("请输入成绩：")
    d = {}
    d['name'] = a
    d['age'] = b
    d['score'] = c
    L.append(d)
print(L)
print("+---------------+----------+----------+")
print("|     name      |   age    |   score  |")
print("+---------------+----------+----------+")
for i in L:
    q = i ['name'].center(15)
    w = str(i['age'].center(10))
    e = str(i['score'].center(10))
    print('|',q,'|',w,'|',e,'|',sep="")
print("+---------------+----------+----------+")
