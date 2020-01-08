class ListHelper01:
    @staticmethod
    def find_all(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_min(list_target, func_condition):
        min = list_target[0]
        for item in range(1, len(list_target)):
            if func_condition(min) > func_condition(list_target[item]):
                min = list_target[item]
        return min

    @staticmethod
    def order_by(list_target, func_condition):
        for r in range(len(list_target) - 1):
            for c in range(r + 1, len(list_target)):
                if func_condition(list_target[r]) < func_condition(list_target[c]):
                    list_target[r], list_target[c] = list_target[c], list_target[r]

    # @staticmethod
    # def remove_skill(list_target, func_condition):
    #     for item in list_target:
    #         if func_condition(item):
    #             list_target.remove(item)

    @staticmethod
    def remove_skill(list_target, func_condition):
        count = 0
        #倒序删除
        for item in range(len(list_target)-1,-1,-1):
            if func_condition(list_target[item]):
                del list_target[item]
                count += 1 #统计删除个数
        return count
