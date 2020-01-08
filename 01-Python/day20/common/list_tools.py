"""
    查找所有
"""

class ListHelper:
    """
       定义对列表的通用操作
    """
    @staticmethod
    def find_all(list_target,func_condition):
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(list_target,func_condition):
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def count(list_target, func_condition):
        int_count = 0
        for item in list_target:
            if func_condition(item):
                int_count += 1
        return int_count

    @staticmethod
    def get_max(list_target, func_condition):
        max = list_target[0]
        for item in range(1,len(list_target)):
            # if list_target[0] < list_target[item]:
            if func_condition(max) < func_condition(list_target[item]):
                max = list_target[item]
        return max

    @staticmethod
    def get_all_count(list_target, func_condition):
        count = 0
        for item in list_target:
            if func_condition(item):
                count += func_condition(item)
        return count

    @staticmethod
    def get_message(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                yield  func_condition(item)

    @staticmethod
    def get_message(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                yield func_condition(item)

    @staticmethod
    def order_by(list_target, func_condition):
        for r in range(len(list_target)-1):
            for c in range(r+1,len(list_target)):
                if func_condition(list_target[r]) > func_condition(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]






