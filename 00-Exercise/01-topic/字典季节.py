seasons = {}
seasons[1]=('春季有1,2,3月')
seasons[2]=('夏季有4,5,6月')
seasons[3]=('秋季有7,8,9月')
seasons[4]=('东季有10,11,12月')

n = int(input("请输入季节1~4:"))
if n in seasons:
    print(seasons[n])
else:
    print("输入有错！")