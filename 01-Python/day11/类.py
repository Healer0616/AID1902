"""
   类，对象
"""
#老婆类
# class Wife01:#类名首字母大写
#     """
#        老婆类
#     """
#     #备注：init方法，前后各有两个下划线
#     def __init__(self,name,age,sex):
#         #self会自动生成地址
#         #数据
#         self.name = name
#         self.age = age
#         self.sex = sex
#     #方法
#     def cooking(self):
#         print("做饭")
# #对象
# w01 = Wife01("铁锤",60,"男")
# w01.cooking()
#
# w02 = Wife01("如花",20,"男")
# w02.cooking()



# class Car01:
#     """
#        #汽车类
#     """
#     def __init__(self,type,speed):
#         self.type = type
#         self.speed = speed
#     def start(self):
#         print("启动")
#     def stop(self):
#         print("停止")
#     def run(self):
#         print("行驶")
# c01 = Car01("宝马",300)
# print(c01)
# c01.start()
# c01.stop()
# c01.run()
#
# c02 = Car01("比亚迪",300)
# print(c02)
# c02.start()
# c02.stop()
# c02.run()



# class Furniture01:
#     def __init__(self,name,size):
#         self.name = name
#         self.size = size
#     def store(self):
#         print("放东西")
# f01 = Furniture01("柜子","大")
# print(f01)
# f01.store()
#
# f02 = Furniture01("箱子","小")
# print(f02)
# f02.store()


# class Zoology01:
#     def __init__(self,name,kind,size):
#         self.name = name
#         self.kind = kind
#         self.size = size
#     def eat(self):
#         print("吃")
#     def run(self):
#         print("奔跑")
# z01 = Zoology01("狮子","猫科动物","大")
# print(z01)
# z01.eat()
# z01.run()
#
# z02 = Zoology01("狗","猫科动物","小")
# print(z02)
# z02.eat()
# z02.run()



#统计ｓｔｕｄｅｎｔ类，总共创建了多少对象


# class Student:
#     count = 0
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#         Student.count += 1
#
# s01 = Student("张三",21)
# Student.get_count()
# s02 = Student("李四",30)
# Student.get_count()
# print(Student.count)

































































































