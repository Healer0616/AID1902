"""
   玩家（具有攻击力）攻击敌人，敌人（具有血量）受伤后掉血，还可能死亡
   敌人攻击玩家，玩家受伤后掉血并碎屏，还可能死亡（游戏结束）
"""

# class Player:
#     def __init__(self,atk,hp):
#         self.atk = atk
#         self.hp =hp
#
#     def attack(self,enemy):
#         enemy.damage(self.atk)
#         print("玩家攻击敌人")
#
#     def damage(self,value):
#         self.hp -= value
#         if self.hp <= 0:
#             self.__death()
#         print("碎屏")
#
#     #私有成员(变量　方法)　类外无法调用
#     def __death(self):
#         print("游戏结束")
#
#
# class Enemy:
#     def __init__(self, atk, hp):
#         self.atk = atk
#         self.hp = hp
#
#     def attack(self, player):
#         print("敌人攻击玩家啦")
#         player.damage(self.atk)
#
#     def damage(self, value):
#         print("敌人受伤啦")
#         self.hp -= value
#         if self.hp <= 0:
#             self.__death()
#
#     # 私有成员(变量　方法)　类外无法调用
#     def __death(self):
#         print("敌人死亡咯")
#
# p01 = Player(10,100)
# e01 = Enemy(5,50)
# e01.attack(p01)
# p01.attack(e01)



"""
   １定义学生类（姓名　成绩）
   
   ２定义根据名称，查找学生对象的方法
       def xxx(list_stu,stu_name):
          ...
   ３创建３个学生对象，指定不同的名字与成绩
   再调用第二步的方法
"""

class Student:
    def __init__(self,id,name,score):
        self.id = id
        self.name = name
        self.score = score
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
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def print_self(self):
        print(self.id,self.name,self.score)

def get_student_by_name(list_stu,stu_name):
    for item in list_stu:
        if item.name == stu_name:
            return item

def get_student_by_id(list_stu,stu_id):
    for item in list_stu:
        if item.id == stu_id:
            return item
    # return None
# 查找成绩大于９０的学生对象
def get_student_by_score(list_stu,stu_score):
    result = []
    for item in list_stu:
        if item.score >= stu_score:
            # item.print_self()
            result.append(item)
    return result
# result = get_student_by_score(list_stu,90)
# for item in result:
#     item.print_self()

list_stu = [
    Student(104,"zs",86),
    Student(102,"ls",100),
    Student(101,"zs",86),
    Student(103,"ww",90),
]

# stu = get_student_by_id(list_stu,101)
# if stu != None:
#     stu.print_self()
# else:
#     print("查无此人")

#查找成绩大于９０的学生对象
# result = get_student_by_score(list_stu,90)
# for item in result:
#     item.print_self()

#查找列表里成绩最高的的学生
# def get_max_by_score(list_stu):
#     max = list_stu[0]
#     for i in range(1,len(list_stu)):
#         if max.score < list_stu[i].score:
#             max = list_stu[i]
#     return max
#
# stu = get_max_by_score(list_stu)
# stu.print_self()

#练习３查找列表中ｉｄ最小的学生
# def get_min_by_id(list_stu):
#     min = list_stu[0]
#     for i in range(1,len(list_stu)):
#         if min.id > list_stu[i].id:
#             min = list_stu[i]
#     return min
#
# stu = get_min_by_id(list_stu)
# stu.print_self()

#练习４在列表中查找指定姓名的学生（同名学生全部查找出来）
# def get_student_by_names(list_stu,stu_name):
#     result = []
#     for item in list_stu:
#         if item.name == stu_name:
#             result.append(item)
#     return result
#
#
# result = get_student_by_names(list_stu,"zs")
# for item in result:
#     item.print_self()

#练习５：将学生列表按招成绩做降序排列（高－>低）
# def order_by_score(list_stu):
#     for r in range(len(list_stu)-1):
#         for c in range(r+1,len(list_stu)):
#             if list_stu[r].score < list_stu[c].score:
#                 list_stu[r],list_stu[c] = list_stu[c],list_stu[r]
#
# order_by_score(list_stu)
# for item in list_stu:
#     item.print_self()















































