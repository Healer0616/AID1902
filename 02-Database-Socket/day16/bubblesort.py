# B排序算法（从小到大排列）
# 1.冒泡排序
# 描述：
#     重复走访要排序是数据依次对比每两个相邻的元素如果次序错误，
#     则交换；重复进行直到没有相邻数据需要交换为止，此时完成排序。
#
# 身高排序10名同学用冒泡排序

# 原始数据value
def bubble(value):
    # 外层循环：对应数据走访的次数
    for i in range(len(value) - 1):
        # 设置初始标志位的值，为False
        flag = False

        # 内层循环：对应每次走访数据时，相邻数据对比次数
        for j in range(len(value) - 1 - i):
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]
                # 若数据发生交换，则置位True
                flag = True

        # 若当前走访数据时，未发生数据交换
        # 则当前数据有序，无需继续走访
        if flag is False:
            break

    # 打印走访次数
    print("走访次数", i + 1)

if __name__ == "__main__":
    # 原始数据
    # value = [180, 230, 149, 260, 130, 170, 160, 169, 163, 178]
    value = [350, 130, 149, 160, 163, 169, 170, 178, 180, 230, 260]
    print("原始数据：", value)
    # 调用排序
    bubble(value)
    print("排序后的数据：", value)