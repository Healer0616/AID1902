"""
    定义学生类分别使用生成器／生成器表达式／列表推导式实现
    计算所有年龄大于２５的学生
    计算所有成绩大于６０的学生
    计算所有成绩大于９０的学生
"""

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

def get_age(stu):
    # result = []
    for item in stu:
        if item.age > 25:
            yield item
    # yield result
stu = [
    StudentModel(1, "zs", 21, 99),
    StudentModel(2, "ls", 26, 88),
    StudentModel(3, "ww", 28, 55),
    StudentModel(4, "zl", 22, 59),
]
# re = get_age(stu)
for item in get_age(stu):
    print(item)
print("..........................")

a = (item for item in stu if item.score > 60)
for item in a:
    print(item)
print("..........................")

s = [item for item in stu if item.score > 90]
for item in s:
    print(item)

# s01 = StudentModel(1, "zs", 21, 99)
# print(s0stu)
# print([s01])
# s02 = eval(repr(s01))
# print(type(s02))

    # def print_self(self):
    #     print(self.id,self.name,self.age,self.score)