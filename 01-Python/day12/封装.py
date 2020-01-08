"""
   封装--私有化
"""


# class Student:
#
#      def __init__(self,name,age):
#          self.set_name(name)
#          self.set_age(age)
#      def get_name(self):
#          return self.__name
#      def set_name(self,value):
#          self.__name = value
#
#      def get_age(self):
#          return self.__age
#
#      def set_age(self,value):
#              self.__age = value
# s01 = Student("张三",23)
# print(s01.get_name())
# print(s01.get_age())



class Student:
    #类的设计者,限制该类对象中只能有如下实例变量
     __slots__ = ("__name","__score","__sex","__age")

     def __init__(self,name,score,sex,age):
         self.name = name
         self.score = score
         self.sex = sex
         self.age = age
     @property
     def name(self):
         return self.__name
     @name.setter
     def name(self,value):
         self.__name = value

     @property
     def score(self):
         return self.__score

     @score.setter
     def score(self, value):
         if 0 <= value <= 100:
             self.__score = value
         else:
             raise ValueError
     @property
     def sex(self):
         return self.__sex
     @sex.setter
     def sex(self,value):
         if value == "男":
             self.__sex = value
         elif value == "女":
             self.__sex = value
         else:
             raise ValueError
     @property
     def age(self):
         return self.__age
     @age.setter
     def age(self,value):
         if 20 <= value <=30:
             self.__age = value
         else:
             raise ValueError
s01 = Student("张三",100,"女",21)
print(s01.name,s01.age,s01.sex,s01.score)
# s01.age = 30
# print(s01.name,s01.age,s01.sex,s01.score)
# print(s01.__dict__)


























































































