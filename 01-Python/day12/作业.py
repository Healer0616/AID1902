"""
   定义技能数据类（技能编号，技能名称，消耗法力，冷却时间，动画名称）
   使用属性进行封装，使用__slots__
"""

# class Skill:
#     __slots__ =("__number","__name","__blue","__cd","__animation")
#     def __init__(self,number = 0,name = "",blue = 0,cd = 0,animation = ""):
#         self.number = number
#         self.name = name
#         self.blue = blue
#         self.cd = cd
#         self.animation = animation
#     @property
#     def number(self):
#         return self.__number
#     @number.setter
#     def number(self,value):
#
#             self.__number = value
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name = value
#     @property
#     def blue(self):
#         return self.__blue
#     @blue.setter
#     def blue(self,value):
#
#             self.__blue = value
#
#     @property
#     def cd(self):
#         return self.__cd
#     @cd.setter
#     def cd(self,value):
#
#             self.__cd = value
#
#     @property
#     def animation(self):
#         return self.__animation
#     @animation.setter
#     def animation(self,value):
#         self.__animation = value
# s01 = Skill(122,"葵花宝典")
# s01.blue = 5
# s01.cd = 8
# s01.animation = "啪"
# print(s01.name)
# print(s01.cd)

"""
   使用代码描述以下场景
   １张三教李四学王者荣耀
   ２李四教张三学ｐｙｔｈｏｎ
   ３李四上班赚了５０００元钱
   最后输出张三具有的技能，李四具有的技能　以及他们的钱
"""

# class Person:
#     # skills 是列表，属于可变对象。作为默认参数后，每次传递的都是同一个列表对象。
#     # 结论：不要给可变数据定义默认参数。
#
#     # def __init__(self,name,skills = [],money = 0):
#     #     self.name = name
#     #     self.skills = skills
#     #     self.money = money
#
#     def __init__(self,name,money = 0):
#         self.name = name
#         # 每次创建一个新列表
#         self.skills = []
#         self.money = money
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         self.__name = value
#
#     @property
#     def skills(self):
#         return self.__skills
#
#     @skills.setter
#     def skills(self,value):
#         self.__skills = value
#
#     @property
#     def money(self):
#         return self.__money
#
#     @money.setter
#     def money(self,value):
#         self.__money = value
#
#     # 张三 教 李四 学王者荣耀。
#     def teach(self,person_other,str_skill):
#
#         person_other.skills.append(str_skill)
#         print(self.name + "教"+person_other.name + str_skill)
#
#     # 李四工作挣了5000元钱
#     def work(self,money):
#         self.money += money
#         print("%s上班,挣了%d钱"%(self.name,money))
#
#
#
# # 张三 教 李四 学王者荣耀。
# zs = Person("张三")
# ls = Person("李四")
# # zs.teach(zs,"王者荣耀")
#
# zs.teach(ls,"王者荣耀")
#
# # 李四 教 张三 学Python
# # ls.teach(ls,"python")
# ls.teach(zs,"python")
#
# # 李四 上班赚了 5000元钱
# ls.work(5000)
# # 最后输出张三具有的技能，李四具有的技能，以及他们的钱。
#
# print(zs.skills,zs.money)
# print(ls.skills,ls.money)


"""
   玩家（具有攻击力）攻击敌人，敌人（具有血量）受伤后掉血，还可能死亡
   敌人攻击玩家，玩家受伤后掉血并碎屏，还可能死亡（游戏结束）
"""

class Player:
    def __init__(self,atk,hp):
        self.atk = atk
        self.hp =hp

    def attack(self,enemy):
        enemy.damage(self.atk)
        print("玩家攻击敌人")

    def damage(self,value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()
        print("碎屏")

    #私有成员(变量　方法)　类外无法调用
    def __death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, player):
        print("敌人攻击玩家啦")
        player.damage(self.atk)

    def damage(self, value):
        print("敌人受伤啦")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    # 私有成员(变量　方法)　类外无法调用
    def __death(self):
        print("敌人死亡咯")

p01 = Player(10,100)
e01 = Enemy(5,50)
e01.attack(p01)
p01.attack(e01)





















































