"""
   技能(编号、名称、法力消耗、冷却时间)
1.	查找指定编号的技能
2.	查找法力消耗大于10的所有技能
-----------------------------------------------------------
3.	查找技能冷却时间最小的技能
4.	根据法力消耗降序排列
5.	删除冷却时间大于10的技能

"""
from common.list_tools02 import ListHelper01
class Skill:
    def __init__(self,id = 0,name = "",blue = 0,cd = 0):
        self.id = id
        self.name = name
        self.blue = blue
        self.cd = cd

    def __repr__(self):  # 给控制器看
        return 'Skill(%d,"%s",%d,%d)' % (self.id, self.name, self.blue, self.cd)

list_sk = [
    Skill(101, "zs", 5, 45),
    Skill(102, "ls", 10, 4),
    Skill(103, "zl", 8, 2),
    Skill(104, "ww", 15, 50),
]

print(ListHelper01.find_all(list_sk,lambda item: item.id == 101))
print("..........................")
print(ListHelper01.find_all(list_sk,lambda item: item.blue > 10))
print("..........................")
print(ListHelper01.get_min(list_sk,lambda item: item.cd))
print("..........................")
ListHelper01.order_by(list_sk,lambda item:item.blue)
for item in list_sk:
    print(item)
print("..........................")
print(ListHelper01.remove_skill(list_sk,lambda item: item.cd > 10))
for item in list_sk:
    print(item)
