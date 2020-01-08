
# class Vector:
#     def __init__(self,x):
#         self.x = x
#
#     def __str__(self):
#         return "向量元素是：%d"% self.x
#           #正向加
#     def __add__(self, other):
#         # return self.x + other
#         return Vector(self.x + other)
#           #反向加
#     def __radd__(self, other):
#         return Vector(self.x + other)
#
# v01 = Vector(1) + 2
# v02 =1 + Vector(1)
# print(v01,v02)

# class Vector:
#     def __init__(self,x):
#         self.x = x
#
#     def __str__(self):
#         return "向量元素是：%d"% self.x
#         #正向减
#     def __sub__(self, other):
#         # return self.x + other
#         return Vector(self.x - other)
#         #反向减
#     def __rsub__(self, other):
#         return Vector(self.x - other)
#
# v01 = Vector(5) - 2
# v02 =1 - Vector(1)
# print(v01,v02)

class Vector:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "向量元素是：%d" % self.x
        #正向乘
    def __mul__(self, other):
        # return self.x + other
        return Vector(self.x * other)
        #反向乘
    def __rmul__(self, other):
        return Vector(self.x * other)

    def __iadd__(self, other):
        self.x += other
        return self

    def __isub__(self, other):
        self.x -= other
        return self

    def __imul__(self, other):
        self.x *= other
        return self

    def __lt__(self, other):
        return self.x < other

    def __eq__(self, other):
        return self.x == other

    def __ne__(self, other):
        return self.x != other

# v01 = Vector(8) * 2
# v02 =9 * Vector(1)
# print(v01,v02)

v09 = Vector(9)
re = v09 != 8
print(re)

v07 = Vector(5)
re = v07 == 5
print(re)

v06 = Vector(9)
re = v06 < 7
print(re)

v05 = Vector(5)
print(id(v05))
v05 += 5
print(id(v05))
print(v05)

v05 = Vector(5)
print(id(v05))
v05 -= 5
print(id(v05))
print(v05)

v05 = Vector(5)
print(id(v05))
v05 *= 5
print(id(v05))
print(v05)