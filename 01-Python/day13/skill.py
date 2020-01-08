# 定义技能数据类(技能编号，技能名称，消耗法力，冷却时间)
# 作业1：在技能数据列表中，查找指定名称的技能对象。
# 作业2：查找冷却时间大于5的所有技能对象。
# 作业3：查找技能数据列表中，消耗法力最小的技能。
# 作业4：查找技能数据列表中，冷却时间最大的技能。
# 作业5：根据冷却时间，对技能列表进行升序(小到大)排列。
"""
   定义技能数据类（技能编号，技能名称，消耗法力，冷却时间）
   使用属性进行封装，使用__slots__
"""

class Skill:
    __slots__ =("__id","__name","__blue","__cd")
    def __init__(self,id = 0,name = "",blue = 0,cd = 0):
        self.id = id
        self.name = name
        self.blue = blue
        self.cd = cd

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):

            self.__id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def blue(self):
        return self.__blue
    @blue.setter
    def blue(self,value):

            self.__blue = value

    @property
    def cd(self):
        return self.__cd
    @cd.setter
    def cd(self,value):
            self.__cd = value

    def print_self(self):
        print(self.id,self.name,self.blue,self.cd)

list_sk = [
    Skill(101, "zs", 5, 60),
    Skill(102, "ls", 10, 4),
    Skill(103, "zl", 8, 2),
    Skill(104, "ww", 15, 45),
]
# 作业1：在技能数据列表中，查找指定名称的技能对象。

# def get_skill_by_name(list_sk,sk_name):
#     for item in list_sk:
#         if item.name == sk_name:
#             return item
#
# sk = get_skill_by_name(list_sk,"zs")
# if sk != None:
#     sk.print_self()
# else:
#     print("查无此人")

# 作业2：查找冷却时间大于5的所有技能对象。
# def get_skill_by_cd(list_sk,sk_cd):
#     result = []
#     for item in list_sk:
#         if item.cd > sk_cd:
#             result.append(item)
#     return result
# result = get_skill_by_cd(list_sk,5)
# for item in result:
#     item.print_self()

# 作业3：查找技能数据列表中，消耗法力最小的技能。
# def get_min_by_skill(list_sk):
#     min = list_sk[0]
#     for item in range(1,len(list_sk)):
#         if min.blue > list_sk[item].blue:
#             min = list_sk[item]
#     return min
# sk = get_min_by_skill(list_sk)
# sk.print_self()

# 作业4：查找技能数据列表中，冷却时间最大的技能。
# def get_max_by_skill(list_sk):
#     max = list_sk[0]
#     for item in range(1,len(list_sk)):
#         if max.blue < list_sk[item].blue:
#             max = list_sk[item]
#     return max
# sk = get_max_by_skill(list_sk)
# sk.print_self()

# 作业5：根据冷却时间，对技能列表进行升序(小到大)排列。
# def order_by_cd(list_sk):
#     for r in range(len(list_sk)-1):
#         for c in range(r+1,len(list_sk)):
#             if list_sk[r].cd > list_sk[c].cd:
#                 list_sk[r],list_sk[c] = list_sk[c],list_sk[r]
# order_by_cd(list_sk)
# for item in list_sk:
#     item.print_self()





























































































