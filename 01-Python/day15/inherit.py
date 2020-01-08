"""
   定义宠物类　数据　姓名
   定义狗类　　数据　工作
   定义猫类　　行为　抓
   分别创键三个类对象调用各自成员
   体会：继承的语法现象
   使用isinstance函数测试各个对象的兼容性
"""
class Pet:
    def __init__(self,name):
        self.name = name

class Dog(Pet):
    def __init__(self,name,work):
        super().__init__(name)
        self.work = work

class Cat(Pet):
    #因为没有数据，所以不需要定义构造函数ｉｎｉｔ
    def grab(self):
        print("抓")
p01 = Pet("莫")
print(p01.name)
c01 = Cat("喵")
print(c01.name)
c01.grab()
print(isinstance(p01,Pet))
