seasons = {1:'春季有1,2,3月',
           2:'夏季有4,5,6月',
           3:'秋季有7,8,9月',
           4:'冬季有10,11,12月'
          }
n = int(input("请输入季度(1~4): "))

if n in seasons:
    print(seasons[n])
else:
    print("输入有错！") 
