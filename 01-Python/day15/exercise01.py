"""
   练习
   若干个有一个圆形（面积：半径平方*ｐｉ）一个矩形（面积：长*宽）
   定义图形管理器：定义记录所有图形（圆形，矩形）的变量
   　　　　　　　定义计算所有图形的面积的方法
   需求变化：可能会增加新的图形（三角形...)
   要求：代码体现开闭原则，依赖倒置原则
   验收：架构图，说出哪里体现了面向对象设计原则
"""
import math

class Graphic:
    # def __init__(self,name):
    #     self.name = name

    def get_area(self):
        """
           获取面积
        :return:
        """
        raise NotImplementedError()


class Circle(Graphic):
    """
       圆形
    """
    def __init__(self,name,radius):
        # super().__init__(name)manager.graphics.append(c01)

        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Graphic):
    """
       矩形
    """
    def __init__(self, name, long, wide):
        # super().__init__(name)
        self.long = long
        self.wide = wide

    def get_area(self):
        return self.long * self.wide

class GraphicManager:
    #记录所有图形
    def __init__(self):
        self.graphics = []

    def add_graphic(self, graphic):
        # graphic 必须是 图形
        if isinstance(graphic, Graphic):
            self.graphics.append(graphic)

    #计算所有图形的总面积
    def get_total_area(self):
        sum = 0
        for item in self.graphics:
            sum += item.get_area()
        return sum


c01 = Circle("大圆形",10)
r01 = Rectangle("矩形",5,8)
manager = GraphicManager()
manager.graphics.append(c01)
manager.graphics.append(r01)

total_area = manager.get_total_area()
print(total_area)





















