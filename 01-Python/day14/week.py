import random

class Person:
    """
       人名
    """
    def __init__(self,name):
        self.name = name

    @staticmethod
    def get(list01):
        i = random.randint(0, 3)
        return (list01[i])

n01 = Person("张三")
n02 = Person("李四")
n03 = Person("王五")
n04 = Person("朱六")
list01 = [n01.name,n02.name,n03.name,n04.name]
# print(list01)
# i = random.randint(0,3)
# print(list01[i])

class And:
    """
       连接词
    """
    def __init__(self,word):
        self.word = word

    @staticmethod
    def get(list01):
        i = random.randint(0, 1)
        return (list01[i])

a01 = And("和")
a02 = And("在")
list02 = [a01.word,a02.word]
# i = random.randint(0,1)
# print(list01[i])


class Site:
    """
       地点
    """
    def __init__(self,site):
        self.site = site

    @staticmethod
    def get(list01):
        i = random.randint(0, 2)
        return (list01[i])

s01 = Site("游乐园")
s02 = Site("高级餐厅")
s03 = Site("澳门赌场")
list03 = [s01.site,s02.site,s03.site]
# i = random.randint(0,2)
# print(list03[i])

class Result:
    """
       结果
    """
    def __init__(self,result):
        self.result = result

    @staticmethod
    def get(list01):
        i = random.randint(0, 1)
        return (list01[i])

r01 = Result("赚了")
r02 = Result("亏了")
list04 = [r01.result,r02.result]
# i = random.randint(0,1)
# print(list04[i])



class Treasure:
    """
       财富
    """
    def __init__(self,money):
        self.money = money
    @staticmethod
    def random():
        import random
        random.randint(1, 10000)
        return random.randint(1, 10000)

class Joint:
    """
       拼接
    """
    @staticmethod
    def print_self():
        list01 = [n01.name, n02.name, n03.name, n04.name]
        a = Person.get(list01)
        b = a01.word
        list01.remove(a)
        l =  random.randint(0,2)
        c = list01[l]
        d = a02.word
        e = Site.get(list03)
        f = Result.get(list04)
        g = Treasure.random()
        print(a+b+c+d+e+f+str(g)+"元")
Joint.print_self()


count = 0
while count <= 15:
    Joint.print_self()
    count += 1




















































