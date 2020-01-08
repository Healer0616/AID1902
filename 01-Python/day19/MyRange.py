for item in range(5):
    print(item)

print("......")


# class My:
#     def __init__(self,num):
#         self.num = num
#     def list_num(self):
#         list01 = []
#         i = 0
#         while i < self.num:
#             list01.append(i)
#             i += 1
#         return list01
#     def __iter__(self):
#         # 1. 创建迭代器对象
#         # 2. 传递需要迭代的数据
#         return MyIterator(self.list_num)
# class MyIterator:
#     def __init__(self,target):
#         self.target = target
#         self.index = 0
#
#     def __next__(self):
#         if self.index >= len(self.target):
#             raise StopIteration()
#
#         item = self.target[self.index]
#         self.index += 1
#         return item
# manager = My(5).list_num()
# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except:
#         break

#迭代器
class MyRangeIterator:
    def __init__(self,stop):
        self.stop = stop
        self.start = 0
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration()
        temp = self.start
        self.start += 1
        return temp

class MyRange:
    def __init__(self,stop):
        self.stop = stop
    def __iter__(self):
        return MyRangeIterator(self.stop)

for item in MyRange(5):
    print(item)


