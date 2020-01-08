class ScoreError(Exception):
    def __init__(self,code,msg):
        super().__init__(msg)
        self.code = code
        self.msg = msg
class Student:
    def __init__(self,score):
        self.score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ScoreError(19,"范围不对")
try:
    s01 = Student(123)
    print(s01.score)
except ScoreError as e:
    print("错误的行数",e.code)
    print("错误的原因", e.msg)



