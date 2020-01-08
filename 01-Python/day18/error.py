"""
   练习：
   定义获取成绩的方法
   要求：如果输入错误，重新输入
   　　　０－－１００
"""
def get_score():
    while True:
        try:
            num = int(input("请输入一个数："))

        except ValueError:
            print("输入有误")
            continue

        if 0 <= num <= 100:
            return num
        print("成绩不在范围内")

print(get_score())

