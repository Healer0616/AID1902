# class MyRangeIterator:
#     def __init__(self, stop):
#         self.stop = stop
#         self.start = 0
#
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration()
#         temp = self.start
#         self.start += 1
#         return temp

class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        # for num in range(0,self.stop):
        #     yield num
        start = 0
        while start < self.stop:
            yield start
            start += 1

for item in MyRange(5):
    print(item)
