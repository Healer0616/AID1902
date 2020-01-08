"""
   学生管理系统
   实现对学生信息的增加　删除　修改　查询
   １增加学生信息
   ２显示学生信息
   ３删除学生信息
   ４修改学生信息
   ５按成绩做升序排列

   数据模型类：StudentModel
   　　数据：编号id　姓名name　年龄age　成绩score
   逻辑控制类：StudentManagerController
　　　　数据：学生列表__list_stu
　　　　行为：学生列表只读属性list_stu　添加学生add_student
　　界面视图类：StudentManagerView
　　　　数据:逻辑控制器对象__controller
　　　　行为：显示菜单__display_menu 选择菜单__selest_menu_item
            输入学生信息__input_student输出学生信息__output_student
"""
class StudentModel:
    """
       学生管理系统
    """
    def __init__(self,id = 0,name = "",age = 0,score = 0):
        """

        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
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
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def __str__(self):#给人看
        return "编号%d,姓名%s,年龄%d,成绩%d" % (self.id, self.name, self.age, self.score)

    def __repr__(self):#给控制器看
        return 'StudentModel(%d,"%s",%d,%d)' % (self.id, self.name, self.age, self.score)

# s01 = StudentModel(1, "zs", 21, 99)
# print(s01)
# print([s01])
# s02 = eval(repr(s01))
# print(type(s02))

    # def print_self(self):
    #     print(self.id,self.name,self.age,self.score)

class StudentManagerController:
    """
       学生核心逻辑控制器
    """
    def __init__(self):
        """
           创建学生管理器对象
        """
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def __generate_id(self):
        #生成编号策略:在最后一个学生编号基础上增加１
        #　　　　　　　如果是第一个学生，则设置为１
        #if语句的真值表达式
        return 1 if len(self.__list_stu) == 0 else self.__list_stu[-1].id + 1

    def add_student(self,stu):
        """
           添加学生对象
        :param stu: 需要添加的学生对象
        :return:
        """
        # stu.id = len(self.__list_stu) + 1
        stu.id = self.__generate_id()
        self.__list_stu.append(stu)

    def remove_student(self,id):
        """
           移除学生
        :param id: 需要移除的学生编号
        :return:
        """
        for item in self.__list_stu:
            if item.id == id:
                self.__list_stu.remove(item)
                return True#表达删除成功
        return False#表达删除失败

    def update_student(self,stu_info):
        #需要修改的学生编号：stu_info.id
        #需要修改的学生信息：stu_info.name stu_info.age ...
        for item in self.__list_stu:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        new_list = self.__list_stu[:]
        for r in range(len(new_list)-1):
            for c in range(r+1,len(new_list)):
                if new_list[r].score < new_list[c].score:
                    new_list[r],new_list[c] = new_list[c],new_list[r]
        return new_list

class StudentManagerView:
    """
        界面视图类
    """
    def __init__(self):
        # 创建学生管理控制器对象
        self.__controller = StudentManagerController()


    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("---------------------")
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩降序显示")
        print("---------------------")

    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        number = input("请输入选项：")
        if number == "1":
            self.__input_students()
        elif number =="2":
            self.__output_student(self.__controller.list_stu)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__output_student_by_score()

    def main(self):
        """
            学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        while True:
            stu = StudentModel()
            stu.name = input("请输入姓名：")
            stu.age = int(input("请输入年龄："))
            stu.score = int(input("请输入成绩："))
            #调用逻辑控制类的添加学生方法
            self.__controller.add_student(stu)
            if input("按y键继续")!= "y":
                break

    def __output_student(self,list_stu):
        """
           在控制台中输出所有学生信息
        :param list_stu: 需要显示的学生列表
        :return:
        """
        for item in list_stu:
            print("%d | %s | %d | %d"%(item.id,item.name,item.age,item.score))

    def __delete_student(self):
        """
           在控制台中删除指定编号的学生
        :return:
        """
        id = int(input("请输入删除学生编号："))
        result = self.__controller.remove_student(id)
        if result:
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        """
           修改学生信息
        :return:
        """
        stu = StudentModel()
        stu.id = int(input("请输入编号："))
        stu.name = input("请输入姓名：")
        stu.age = int(input("请输入年龄："))
        stu.score = int(input("请输入成绩："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        """
           按照成绩降序显示
        :param list_stu:
        :return:
        """
        result = self.__controller.order_by_score()
        self.__output_student(result)

view = StudentManagerView()
view.main()