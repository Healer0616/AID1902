
# 2.二分查找
# 描述：（从小到大）12345->4
# 找出**有序**数据中的中间元素，由中间元素将数据分成左右两部分，比较中间元素与待查找值的大小
# 如果相等，则查找成功；
# 如果中间元素比查找元素值大，则继续在左侧重复该过程；
# 如果中间元素比查找元素值小，则继续在右则重复该过程；
# 如此递归下去，直到成功找到或者查找完所有数据为止。


# 扑克牌54，只取红桃13张用1 - 13，将13张牌从小到大排列然后翻面朝上。找到红桃6.怎么找？

# 二分查找

# 使用递归实现

# 原始数据 value
# [1,2,3,4,5,6,7,8,9,10,11,12,13]
# 待查找数据 key - 6
# 当前查找范围左侧数据对应下标值 left
# 当前查找范围右侧数据对应下标值 right
def binary(value, key, left, right):
    # 递归退出条件
    if left > right:
        # 查找结束 - 查找失败
        return -1

    # 获取中间元素对应下标
    middle = (left + right) // 2
    # 对比中间数据值与待查找值
    if value[middle] == key:
        # 查找成功  返回对应下标值
        return middle
    elif value[middle] > key:
        # 中间数据值大于待查找值时
        # 继续在左侧重复该过程
        # 查找范围缩小：左侧不变，右侧下标值变为中间元素的前一位
        return binary(value, key, left, middle - 1)
    else:
        # 中间数据值小于待查找值时
        # 继续在右侧重复该过程
        # 查找范围缩小：右侧不变，左侧下标值变为中间元素的前一位
        return binary(value, key, middle + 1, right)

if __name__ == "__main__":
    # 原始数据 value
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # 待查找数据 key
    key = 6
    # 调用二分查找
    res = binary(value, key, 0, len(value) - 1)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功", res)