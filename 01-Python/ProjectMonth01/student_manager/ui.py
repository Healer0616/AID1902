"""
   学生管理系统界面视图类
"""
import models
import bll
class StudentManagerView:
    """
        界面视图类
    """
    def __init__(self):
        # 创建学生管理控制器对象
        self.__controller = bll.StudentManagerController()


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

    def __input_int(self,msg):
        """
           异常处理
        :param msg:
        :return:
        """
        while True:
            try:
                return int(input(msg))
            except:
                print("输入有误")

    def __input_students(self):
        while True:
            stu = models.StudentModel()
            stu.name = input("请输入姓名：")
            stu.age = self.__input_int("请输入年龄：")
            stu.score = self.__input_int("请输入成绩：")
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
        id = self.__input_int("请输入删除学生编号：")
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
        stu = models.StudentModel()
        stu.id = self.__input_int("请输入编号：")
        stu.name = input("请输入姓名：")
        stu.age = self.__input_int("请输入年龄：")
        stu.score = self.__input_int("请输入成绩：")
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