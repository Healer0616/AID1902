from common.list_tools import ListHelper
class StudentModel:
    """
       学生管理系统
    """
    def __init__(self,id = 0,name = "",age = 0,score = 0):
        """

        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):#给控制器看
        return 'StudentModel(%d,"%s",%d,%d)' % (self.id, self.name, self.age, self.score)
stu = [
    StudentModel(1, "zs", 21, 99),
    StudentModel(2, "ls", 26, 88),
    StudentModel(3, "ww", 28, 55),
    StudentModel(4, "zl", 22, 59),
]


# from common.list_tools import ListHelper

def condition01(item):
    return item.age < 30

def condition02(item):
    return item.name == "zs"

def condition03(item):
    return item.name == "zs"

for item in ListHelper.find_all(stu,condition01):
    print(item)
print("..........................")
print(ListHelper.first(stu,condition02))
print("..........................")
print(ListHelper.count(stu,lambda item: item.name == "zs"))
print("..........................")
print(ListHelper.first(stu,lambda item:item.id == 1))
print("..........................")
for item in ListHelper.find_all(stu,lambda item:item.score < 60):
    print(item)
print("..........................")
for item in ListHelper.find_all(stu,lambda item:item.age > 20 and item.score >  60):
    print(item)
print("..........................")
print(ListHelper.get_max(stu,lambda item:item.age))
print("..........................")
print(ListHelper.get_max(stu,lambda item:item.score))
print("..........................")
print(ListHelper.get_all_count(stu,lambda item:item.score))
print("..........................")
print(ListHelper.get_all_count(stu,lambda item:item.age))
print("..........................")
for item in ListHelper.get_message(stu,lambda item:item.name):
    print(item)
print("..........................")
for item in ListHelper.get_message(stu,lambda item:item.age):
    print(item)
print("..........................")
for item in ListHelper.get_message(stu,lambda item:item.score):
    print(item)
print("..........................")
ListHelper.order_by(stu,lambda item:item.score)
for item in stu:
    print(item)
print("..........................")
ListHelper.order_by(stu,lambda item:item.age)
for item in stu:
    print(item)