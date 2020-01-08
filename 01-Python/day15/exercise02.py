"""
　　一家公司有如下几种岗位　
　　程序员：底薪＋项目分红
　　软件测试：底薪＋ｂｕｇ数*５
　　销售：底薪＋销售额*5%
　　定义员工管理器，记录所有员工，计算所有员工的总薪资
　　要求:增加新的岗位，员工管理器满足开闭原则
　　画出架构图，写出体现依赖倒置原则，开闭原则的点
"""

class Company:
    """
       公司
    """
    def get_all_money(self):
        raise NotImplementedError()

class Programmer(Company):
    """
       程序员
    """
    def __init__(self,value,bonus):
        self.value = value
        self.bonus = bonus

    def get_all_money(self):
        return self.value + self.bonus

class Software_testing(Company):
    """
       软件测试
    """
    def __init__(self,value,bug):
        self.value = value
        self.bug = bug

    def get_all_money(self):
        return self.value + self.bug * 5

class Market(Company):
    """
       销售
    """
    def __init__(self,value,sale):
        self.value = value
        self.sale = sale

    def get_all_money(self):
        return self.value + self.sale * 0.05

class StaffManager:
    """
       员工管理器
    """
    def __init__(self):
        self.staff = []

    def add_staff(self, staff):
        # staff 必须是 员工
        if isinstance(staff, Company):
            self.staff.append(staff)

    def get_all_moneys(self):
        sum = 0
        for item in self.staff:
            sum += item.get_all_money()
        return sum

# p01 = Programmer(3000,1000)
# s01 = Software_testing(2000,100)
# m01 = Market(2000,10000)

manager = StaffManager()
manager.add_staff(Programmer(10000,20000))
manager.add_staff(Software_testing(2000,100))
manager.add_staff(Market(2000,10000))
manager.add_staff("mmp")

total_staff = manager.get_all_moneys()
print(total_staff)



