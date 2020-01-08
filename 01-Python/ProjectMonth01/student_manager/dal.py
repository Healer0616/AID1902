"""
   Data   数据
   Access　访问
   Layer　　层
"""
#1.保存学生列表（由ｂｌｌ层的添加／删除／修改方法调用）
#2.加载学生列表（ｂｌｌ层的Controller类构造函数）

#常量：不允许修改的数值
FILE_PATH = "list_stu.txt"

from models import StudentModel
import os

class TextDao:
    """
       文本文件　数据访问对象
    """
    @staticmethod
    def save_student_list(list_stu):
        with open(FILE_PATH,"w",encoding="utf-8") as stu_file:
            for stu in list_stu:
                stu_file.write(stu.__repr__() + "\n")

    @staticmethod
    def load_student_list():
        list_stu = []
        #如果文件不存　则退出
        if not os.path.isfile(FILE_PATH):
            return list_stu

        with open(FILE_PATH, "r", encoding="utf-8") as stu_file:
            for line in stu_file:
                stu = eval(line)
                list_stu.append(stu)
        return list_stu

#测试----------------------------------------------
# from models import StudentModel
#
# list_stu = [
#     StudentModel(101,"ZS",20,100),
#     StudentModel(101,"ls",25,79),
#     StudentModel(101,"ww",27,80),
#     StudentModel(101,"zl",28,99),
# ]
# TextDao.save_student_list(list_stu)
#
# for item in TextDao.load_student_list():
#     print(item)

