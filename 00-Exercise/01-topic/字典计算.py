s=input("请输入:")
d={}
for x in s:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1

for k in d:
    print(k , ':' , d[k] , '次' )
