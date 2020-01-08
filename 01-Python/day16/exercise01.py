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

    def __str__(self):
        return "编号%d,姓名%s,年龄%d,成绩%d"%(self.id,self.name,self.age,self.score)

    def __repr__(self):
        return 'StudentModel(%d,"%s",%d,%d)'%(self.id,self.name,self.age,self.score)
s01 = StudentModel(1, "zs", 21, 99)
print(s01)
print([s01])
s02 = eval(repr(s01))
print(type(s02))
